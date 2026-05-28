# Product Requirements Document (PRD)

## Project: College Algebra Activity Designer

---

## 1. Problem Statement

A university mathematics instructor teaching college algebra spends significant time and
creative energy designing collaborative in-class activities. The core pain points are:

- **Ideation bottleneck:** Coming up with fresh, engaging activity formats is difficult.
  Most ideas default to card sorts, which become repetitive for students.
- **Structural collaboration gap:** Students naturally work independently unless the
  activity design *forces* them to collaborate. Most activity designs fail to build in
  structural interdependence.
- **Difficulty calibration:** Activities need to be rigorous enough to be meaningful but
  accessible to students with college algebra preparation. This balance is hard to
  achieve consistently.
- **Time constraint:** Class periods are exactly 50 minutes. Collaborative activities
  must fit within approximately 30 minutes (introduction through completion), leaving
  time for transitions and debrief.
- **Resource underuse:** The instructor has access to large tabletop whiteboards,
  individual student markers, math manipulatives, printers, scissors, and standard
  office supplies — but these are underused beyond basic card sorts.

---

## 2. User

**Primary user:** One university mathematics instructor (expert in mathematics education,
full-time faculty at a 4-year university).

**Usage context:** Planning sessions before class, typically working alone at a computer.
The instructor wants to describe what they need and receive a ready-to-use (or
near-ready) activity, or paste in a draft and receive structured feedback.

---

## 3. In Scope (Prototype)

- Generate new collaborative activities for the **rational functions** unit of college
  algebra
- Evaluate and provide structured feedback on instructor-drafted activities
- Enforce the 30-minute time constraint
- Enforce structural collaboration requirements
- Map activities to available physical resources
- Export activities as formatted text or Markdown

---

## 4. Out of Scope (Prototype)

- Other college algebra topics (polynomials, exponentials, etc.) — added later
- Student-facing interfaces
- Learning management system (LMS) integration
- Grading or assessment features
- Activities longer than 30 minutes

---

## 5. Requirements

### REQ-01: Activity Generation
**Pain point:** Ideation bottleneck  
**Specification:** Given a topic, learning objectives, and constraints, the system
generates a complete activity including: title, overview, materials needed, step-by-step
instructions, discussion prompts, and a facilitator guide.  
**Value:** Reduces activity design time from hours to minutes.

### REQ-02: Activity Evaluation
**Pain point:** Difficulty calibration, structural collaboration gap  
**Specification:** Given an instructor-drafted activity, the system returns structured
feedback across five dimensions: mathematical rigor, accessibility, structural
collaboration, timing, and resource use.  
**Value:** Gives the instructor a second opinion before class, catching issues that are
easy to overlook.

### REQ-03: Structural Collaboration Enforcement
**Pain point:** Students work independently unless forced to collaborate  
**Specification:** Every generated activity must include at least one mechanism that
makes it *impossible* (or significantly harder) to complete without collaboration.
Examples: jigsaw information structure, role assignments, split resources.  
**Value:** Ensures activities achieve their pedagogical purpose.

### REQ-04: Timing Validation
**Pain point:** 50-minute class period constraint  
**Specification:** Every activity must include a time estimate broken down by phase
(introduction, group work, debrief). Total must not exceed 30 minutes.  
**Value:** Prevents activities from running over and disrupting the class schedule.

### REQ-05: Resource Mapping
**Pain point:** Physical resources are underused  
**Specification:** Activities should specify which physical resources are used and why.
The system should prioritize using whiteboards, markers, and manipulatives creatively.  
**Value:** Increases engagement and makes better use of available materials.

### REQ-06: Rational Functions Coverage
**Pain point:** Topic-specific rigor  
**Specification:** Generated activities must address one or more of: simplifying rational
expressions (including factoring), holes, vertical asymptotes, horizontal asymptotes,
x-intercepts, y-intercepts. No oblique asymptotes (polynomial division not covered).  
**Value:** Ensures alignment with course curriculum.

---

## 6. Success Criteria

- A generated activity requires no more than 5 minutes of instructor editing before use
- Evaluation feedback is specific enough to act on (not generic)
- Every activity includes a structural collaboration mechanism
- Time estimates are accurate within ±5 minutes
- The instructor reports higher creative confidence after using the tool

---

## 7. Out of Scope Decisions Log

| Decision | Reason |
|----------|--------|
| No oblique asymptotes | Polynomial division not covered in this course |
| No graphing from equations | Out of scope for this unit's learning objectives |
| No student-facing UI | Prototype is instructor-only |