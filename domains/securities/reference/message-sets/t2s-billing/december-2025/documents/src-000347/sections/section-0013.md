---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Functionality"]
content_origin: "source-transcription"
---

# Functionality

Source: [src-000347](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`. Locator: heading path Scope and Functionality / Groups of MessageDefinitions and Functionality / Functionality.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P77** Functionality

**P78** These Billing messages definitions are specifically designed to support the following technical functions:

**P79** Billing Report Request: the camt.076 is sent to make the following types of queries:

**P80** Cumulative Billing Data Query enabling the sender to request the billing data of an invoice, which consists of the aggregated information on the level of a System Member for a specified period for each offered functionality;

**P81** Itemised Billing Data Query enabling the sender to request itemised billing data information which consists of the aggregated information on the level of a single securities account, cash account or party within a given period for each service item.

**P82** Billing Report: the camt.077 is sent to provide with:

**P83** the official invoice;

**P84** status of a previously sent cancellation of the latest valid invoice;

**P85** consumption data message (for NCBs only);

**P86** response to a user query containing billing data.

**P87** The BillingReport message is sent in push mode (invoice, invoice cancellation and consumption message) or as response to the Billing Report Request camt.076 message, containing information on requested items (cumulative or itemised billing data) or business error reports.

**P89** See Message Definition Report Part 2 for the message and formats.

