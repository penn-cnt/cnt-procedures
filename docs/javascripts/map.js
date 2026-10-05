/* Wiki map: one force graph, three groupings (theme / stage / role).
   Data comes from map/graph.json, generated at build time from page front matter. */
(function () {
  const THEME_COLORS = {
    "Data": "#2a78d6", "Compute": "#eb6834", "Imaging": "#1baf7a",
    "Electrophysiology": "#eda100", "REDCap & Clinical Metadata": "#e87ba4", "Operations": "#008300"
  };

  async function boot() {
    const host = document.getElementById("wiki-map");
    if (!host || host.dataset.ready) return;
    host.dataset.ready = "1";
    const d3 = await import("https://cdn.jsdelivr.net/npm/d3@7/+esm");
    const root = location.pathname.replace(/map\/?(index\.html)?$/, "");
    const data = await (await fetch(root + "map/graph.json", { cache: "no-store" })).json();

    const views = {
      theme: { label: "Theme", hubs: data.themes, of: n => [n.theme] },
      stage: { label: "Stage", hubs: data.stages, of: n => [n.stage] },
      role:  { label: "Role",  hubs: Object.keys(data.roles), of: n => n.roles,
               name: k => (data.roles[k] ? data.roles[k][0] : k) },
    };
    if (data.scopes && Object.keys(data.scopes).length) {
      views.scope = { label: "Scope", hubs: Object.keys(data.scopes), of: n => [n.scope || "core"], name: k => data.scopes[k] || k };
    }
    let view = (location.hash.replace("#", "") in views) ? location.hash.replace("#", "") : "theme";
    let query = "";

    host.innerHTML = `
      <div class="wm-bar">
        <div class="wm-switch" role="tablist">
          ${Object.entries(views).map(([k, v]) => `<button data-view="${k}" role="tab">${v.label}</button>`).join("")}
        </div>
        <input class="wm-search" type="search" placeholder="Filter pages…" aria-label="Filter pages">
        <span class="wm-count"></span>
      </div>
      <div class="wm-legend"></div>
      <div class="wm-canvas"><svg></svg><div class="wm-tip" hidden></div></div>`;
    const svg = d3.select(host).select("svg");
    const tip = host.querySelector(".wm-tip");
    const color = t => THEME_COLORS[t] || "#888";

    host.querySelector(".wm-legend").innerHTML = data.themes.map(t =>
      `<span class="wm-key"><i style="background:${color(t)}"></i>${t}</span>`).join("") +
      `<span class="wm-key wm-key-note">node = one procedure · colour = theme · drag to rearrange · click to open</span>`;

    const W = host.clientWidth || 900, H = Math.max(560, Math.min(820, window.innerHeight - 260));
    svg.attr("viewBox", [0, 0, W, H]).attr("width", "100%").attr("height", H);
    const g = svg.append("g");
    const linkL = g.append("g").attr("class", "wm-links");
    const nodeL = g.append("g").attr("class", "wm-nodes");
    const hubL = g.append("g").attr("class", "wm-hubs");

    const zoomer = d3.zoom().scaleExtent([0.4, 3]).on("zoom", e => g.attr("transform", e.transform));
    svg.call(zoomer);
    const sim = d3.forceSimulation()
      .force("link", d3.forceLink().id(d => d.id).distance(d => 55 + 1.2 * Math.sqrt(d.target.count || 1)).strength(0.6))
      .force("charge", d3.forceManyBody().strength(d => d.hub ? -900 : -30).distanceMax(500))
      .force("collide", d3.forceCollide(d => d.hub ? 78 : 8.5).strength(0.9))
      .force("x", d3.forceX(W / 2).strength(0.04))
      .force("y", d3.forceY(H / 2).strength(0.06));

    function fit() {                      // zoom so the whole graph is visible
      const ns = sim.nodes(); if (!ns.length) return;
      const xs = ns.map(n => n.x), ys = ns.map(n => n.y);
      const x0 = Math.min(...xs) - 60, x1 = Math.max(...xs) + 60, y0 = Math.min(...ys) - 60, y1 = Math.max(...ys) + 70;
      const k = Math.min(1.6, 0.95 * Math.min(W / (x1 - x0), H / (y1 - y0)));
      const t = d3.zoomIdentity.translate(W / 2 - k * (x0 + x1) / 2, H / 2 - k * (y0 + y1) / 2).scale(k);
      svg.call(zoomer.transform, t);
    }

    function render() {
      const v = views[view];
      host.querySelectorAll(".wm-switch button").forEach(b => b.setAttribute("aria-selected", b.dataset.view === view));
      const q = query.trim().toLowerCase();
      const pages = data.nodes.filter(n => !q || (n.title + " " + n.section + " " + n.theme + " " + n.stage + " " + n.roles.join(" ")).toLowerCase().includes(q));
      const hubs = v.hubs.map(h => ({ id: "hub:" + h, hub: true, key: h, title: v.name ? v.name(h) : h,
                                      count: pages.filter(n => v.of(n).includes(h)).length }));
      const nodes = hubs.concat(pages.map(n => Object.assign({}, n)));
      const links = [];
      pages.forEach(n => v.of(n).forEach(h => { if (v.hubs.includes(h)) links.push({ source: n.id, target: "hub:" + h, theme: n.theme }); }));
      host.querySelector(".wm-count").textContent = `${pages.length} procedures`;

      const prev = new Map(sim.nodes().map(n => [n.id, n]));
      nodes.forEach(n => { const p = prev.get(n.id); if (p) { n.x = p.x; n.y = p.y; n.vx = p.vx; n.vy = p.vy; } });
      hubs.forEach((h, i) => { if (!prev.get(h.id)) { const a = -Math.PI / 2 + i * 2 * Math.PI / hubs.length;
        h.x = W / 2 + Math.cos(a) * Math.min(W, H) * 0.34; h.y = H / 2 + Math.sin(a) * Math.min(W, H) * 0.34; } });

      const link = linkL.selectAll("line").data(links, d => d.source + "→" + d.target);
      link.exit().remove();
      link.enter().append("line").merge(link)
        .attr("stroke", d => color(d.theme)).attr("stroke-opacity", 0.28).attr("stroke-width", 1);

      const node = nodeL.selectAll("circle").data(nodes.filter(n => !n.hub), d => d.id);
      node.exit().remove();
      node.enter().append("circle").attr("r", 5.5).attr("stroke", "var(--md-default-bg-color)").attr("stroke-width", 1.5)
        .on("click", (e, d) => { location.href = root + d.url; })
        .on("mousemove", (e, d) => {
          tip.hidden = false;
          tip.innerHTML = `<b>${d.title}</b><br>${d.theme} › ${d.section}<br><span>${d.stage}</span><br><span>${d.roles.map(r => (data.roles[r] || [r])[0]).join(" · ")}</span>${d.scope ? `<br><span>${(data.scopes && data.scopes[d.scope]) || d.scope}</span>` : ""}`;
          const r = host.querySelector(".wm-canvas").getBoundingClientRect();
          tip.style.left = (e.clientX - r.left + 14) + "px"; tip.style.top = (e.clientY - r.top + 14) + "px";
        })
        .on("mouseleave", () => { tip.hidden = true; })
        .call(drag(sim))
        .merge(node).attr("fill", d => color(d.theme)).style("cursor", "pointer");

      const hub = hubL.selectAll("g").data(hubs, d => d.id);
      hub.exit().remove();
      const hubEnter = hub.enter().append("g").call(drag(sim));
      hubEnter.append("circle").attr("r", 30);
      hubEnter.append("text").attr("class", "wm-hub-n").attr("text-anchor", "middle").attr("dy", 5);
      hubEnter.append("text").attr("class", "wm-hub-t").attr("text-anchor", "middle").attr("dy", 48);
      const hubAll = hubEnter.merge(hub);
      hubAll.select("circle").attr("fill", "var(--md-default-bg-color)")
        .attr("stroke", d => view === "theme" ? color(d.key) : "var(--md-default-fg-color--light)").attr("stroke-width", 4);
      hubAll.select(".wm-hub-n").text(d => d.count);
      hubAll.select(".wm-hub-t").text(d => d.title);

      const ticked = () => {
        linkL.selectAll("line").attr("x1", d => d.source.x).attr("y1", d => d.source.y).attr("x2", d => d.target.x).attr("y2", d => d.target.y);
        nodeL.selectAll("circle").attr("cx", d => d.x).attr("cy", d => d.y);
        hubAll.attr("transform", d => `translate(${d.x},${d.y})`);
      };
      sim.nodes(nodes).on("tick", ticked);
      sim.force("link").links(links);
      // settle synchronously so the view opens laid out and fitted, then stay warm for dragging
      sim.stop(); sim.alpha(1);
      for (let i = 0; i < 320; i++) sim.tick();
      ticked(); fit();
      sim.alpha(0.05).restart();
    }

    function drag(sim) {
      return d3.drag()
        .on("start", (e, d) => { if (!e.active) sim.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; })
        .on("drag", (e, d) => { d.fx = e.x; d.fy = e.y; })
        .on("end", (e, d) => { if (!e.active) sim.alphaTarget(0); if (!d.hub) { d.fx = null; d.fy = null; } });
    }

    host.querySelectorAll(".wm-switch button").forEach(b => b.addEventListener("click", () => { view = b.dataset.view; history.replaceState(null, "", "#" + view); render(); }));
    host.querySelector(".wm-search").addEventListener("input", e => { query = e.target.value; render(); });
    window.addEventListener("hashchange", () => { const h = location.hash.replace("#", ""); if (h in views && h !== view) { view = h; render(); } });
    render();
  }

  if (window.document$) { window.document$.subscribe(boot); } else { document.addEventListener("DOMContentLoaded", boot); }
})();
