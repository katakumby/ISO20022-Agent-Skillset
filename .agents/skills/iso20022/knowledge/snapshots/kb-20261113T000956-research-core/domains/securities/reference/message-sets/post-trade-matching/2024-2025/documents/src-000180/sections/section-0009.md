---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["Scope and Functionality", "Scope"]
content_origin: "source-transcription"
---

# Scope

Source: [src-000180](../../../../../../../../../evidence/omitted/620693d01e301c06503cea9a.md). Locator: heading path Scope and Functionality / Scope.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P75** Scope

**P76** This project will cover only the first phase of the post trade/pre-settlement program with activities of the securities trade lifecycle on the client side being concentrated on with minimal exception.  Subsequent business justifications will be submitted to cover 1) Clearing activities and 2) Collateral Management. These additional projects will be documented in detail in separate work plan and business requirement documents.

**P77** The scope of the project is currently defined as to include the following:  

[T6 - complete table](../tables/tbl-0006.md)

**P80** The scope of processing to be covered by the Post-Trade messages includes the business processes from trade notification through confirmation/affirmation. Although we are still analysing the requirements, we expect to design approximately 10 messages to cover the business processes described above: 

**P81** Notice/Advise Of Execution (+ Cancellation and Modification)

**P82** Allocation Instruction (+Allocation Cancellation & Modification)

**P83** Allocation Report/Details (+ cancellation & modification)

**P84** Matching Status (Accept Trade/Reject Trade/Trade Status/ Confirmation Reject)

**P85** Confirmation (+ Confirmation Cancellation and Modification)

**P86** Affirmation 

**P87** The following diagram is an illustration of the primary communication flows which this business justification is addressing (the green is what is in scope).

[fig-0001 - original figure evidence](../diagrams/fig-0001.md)

**P91** In the current environment, Post-Trade communication, as scoped, is mainly supported by the following ISO 15022 messages as well as a number of proprietary message formats:MT509 – Trade Status Message

**P92** MT513 – Client Advice of Execution

**P93** MT514 – Trade Allocation Instruction

**P94** MT515 – Client Confirmation of Purchase or Sale

**P95** MT517 – Trade Confirmation Affirmation

**P96** New ISO 20022 messages are expected to be reverse-engineered from current industry practices, ISO 15022 standards and the FIX standard. Additional messages, functionality and information will be added to support defined functionality as determined by industry participants.

