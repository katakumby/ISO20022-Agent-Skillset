---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.2 Message Datatypes", "9.2.2 CodeSet", "9.2.2.25 ModificationProcessingStatus1Code"]
file_pages: [331]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.2.2.25 ModificationProcessingStatus1Code

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 331 to 331.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 331

```text
9.2.2.25  ModificationProcessingStatus1Code
Definition: Specifies the status of a cancellation request.
Type: CodeSet
CodeName Name Definition
PACK Accepted Modification request has been
acknowledged for further processing by
the account servicer.
REJT Rejected Modification has been rejected for further
processing.
MODC Completed Modification has been completed.
DEND Denied Modification will not be executed.
MODP Pending Modification is pending. It is not known
at this time whether modified can be
executed.
REPR InRepair Modification request is in repair.
9.2.2.26  MovementResponseType1Code
Definition: Specifies the type of movement response to be returned.
Type: CodeSet
CodeName Name Definition
FULL Full Response will include full details on the
movements reported.
STTS Status Response will include limited details
including the status on the movements
reported.
9.2.2.27  NoReasonCode
Definition: Specifies that there is no reason available.
Type: CodeSet
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
9.2.2.28  OptionStyle2Code
Definition: Defines how an option can be exercised.
Type: CodeSet
CodeName Name Definition
AMER American Option can be exercised before or on
expiry date.
EURO European Option that can be exercised on expiry
date only.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 331 September 2025
```

