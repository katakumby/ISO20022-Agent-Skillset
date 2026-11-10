---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000343"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Administration"]
content_origin: "source-transcription"
---

# Administration

Source: [src-000343](../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart1_Target2Securities_Administration_2023_2024_v2.docx`. Locator: heading path Scope and Functionality / Groups of MessageDefinitions and Functionality / Groups / Administration.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P83** Administration

**P84** This Administration message set consists of:

[T4 - complete table](../tables/tbl-0004.md)

**P86** This Administration message set consists of the Report Query Request (admi.005) and Resend Request (admi.006) and Receipt Acknowledgement (admi.007). The Report Query Request and the Resend Request will be used with the ISO 20022 Business Application Header (head.001). 

**P87** The ReceiptAcknowledgement message is in general sent by T2S without BAH. Only in case it is sent as response to the Report Query Request (admi.005) the BAH is attached.  

**P88** The business scenarios for which a BAH is not provided are: Missing Authentication; Inbound Processing Rejections; Oversize and timeout scenarios and query queuing information. 

**P90** The Business File Header (head.002) can be used to bundle multi messages within a file.  A Business File can contain one or several business messages (Business Application & ISO message). In response to an incoming Business File a ReceiptAcknowledgement (admi.007) will be sent, to provide information on negative validation for a certain business message or the whole Business File.

**P91** See Message Definition Report Part 2 for the message and formats.

