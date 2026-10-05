---
title: "Grid Electrode Labeling Conventions"
stage: "Data Standardization & Integration"
roles: [data-rc, analyst]
audit: merge
order: 5
---

# Grid Electrode Labeling Conventions

!!! abstract "What this page tells you"
    How to label a grid electrode in voxtool: set dimensions as contacts-per-row by rows, label the four corners with matching label numbers and X/Y lead coordinates (worked 8x4 example), then interpolate, repeating or manually filling missed contacts. Links a video tutorial.

#### Labeling Grids

*   Based on an example of an 8X8 grid split after the 4th row. The dimensions are x: 8(contacts per row) , y :4 (rows)
*   The X dimension represents column point (row corners : 1-8), the Y dimension represents the row points ( 1-4) 
*   Label grid by corners: First corner is (1,1), 2nd corner is (1,8). <— you are still in the first row (#1), and you are labeling the 8th electrode of that row (#8) .
*   When labeling the 8th electrode of the first row (aka: the 2nd corner), change the X Label number to 8 (or the Nth electrode of the row), and the Lead number to match.
*   Labeling the 3rd corner- change the label # to the Nth electrode contact of that row  corresponding to that corder( in this case this is contact #25). And change the lead X Lead to 1, representing the Nth electrode of that row.  The Y Lead will be changed to 4, to represent you are labling in the 4th row. In this case this is the 1st point on the 4th row.  Lead coordinates will be as follows : (X: 1,Y:4)
*   Labeling the 4th corder- change the Label to the Nth electrode contact corresponding to that corner, in this case this is the final and 32nd contact. (Label 32). The X Lead is corresponding to which electrode in the row you are selecting (x=8) in. The Y coordinate will represent the row that you located in (y=4). Your Lead coordinates will be as follows ( X: 8, Y:4)
*   When all four corners have been labeled, you can interpolate. 
*   If electrodes are not found with first interpolation, click interpolate again to see if it continues to find electrodes within rage (it should find the remainder of electrodes)
*   If the interpolation misses an electrode, you can manually input the electrode you are working on by defining the x coordinate (which electrode in the row you are on), and y coordinate (which row you are located in), as well as the label number (the Nth electrode in the grid that you are labeling)

#### See tutorial below:
<span class="attachment-note" title="Too large for the Git repository">🎬 Video: video1338425901.mp4 — kept in Dropbox › NeuroBridge › wiki-media as <code>7927-video1338425901.mp4</code></span>
