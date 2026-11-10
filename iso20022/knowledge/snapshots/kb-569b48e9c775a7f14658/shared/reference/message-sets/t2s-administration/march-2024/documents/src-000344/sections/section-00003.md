---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [3]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.005.001.02", "admi.006.001.01", "admi.007.001.01"]
---

# 1 Message Set Overview

Source: [src-000344](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 3 to 3.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3

```text
1 Message Set Overview
Introduction
This document describes the Target2-Securities - Administration message set. It includes the new
version of the MessageDefinitions that have been added as part of the maintenance cycle 2023-2024
(See MCR #234) and approved by the Securities and the Payments Standards Evaluation Groups
under the leadership of the Securities SEG on 15 February 2024.
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
admi.005.001.02
ReportQueryRequestV02
The ReportQueryRequest message is exchanged
between system member and system transaction
administrator.
It aims at querying the latest available report data of a
specific report type. A report is stored and available for
query until the event occurs again report is replaced.
admi.006.001.01
ResendRequestV01
A system member or any parties authorised by them
send a ResendRequest message to the Central
System (such as the T2S platform). The purpose of
this request is, that the requesting party wants to
receive the "original" message once again. This might
be caused through technical problems on the receiving
side (message could not be received or processed or
is missing in the message sequencing) or for archiving
purposes.
admi.007.001.01
ReceiptAcknowledgementV01
The ReceiptAcknowledgement message is sent by the
transaction administrator to a member of the system
and vice versa. It is sent to acknowledge the receipt of
one or multiple messages sent previously. The
Acknowledgement message is 1) an application receipt
acknowledgement and 2) conveys information about
the processing of the original message(s). In case of 2)
the ReceiptAcknowledgement can be used as a
Generic error message, which provides information
about the status (e.g. rejection, acceptance) of an
instruction.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Set Overview
Target2-Securities - Administration - Maintenance 2023 -
2024
3 March 2024
```

