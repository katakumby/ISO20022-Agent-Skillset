---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.16 Status", "17.1.16.18 CancellationReason19Choice", "17.1.16.18.2 Proprietary <Prtry>"]
file_pages: [448]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.16.18.2 Proprietary <Prtry>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 448 to 448.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 448

```text
CodeName Name Definition
CANZ CancelledSplitPartialSettlement Original transaction has been cancelled
and replaced to allow a partial or split
settlement.
CORP CancelledDueToCorporateAction Transaction has been cancelled due to a
corporate action.
SCEX SecuritiesNoLongerEligible Transaction has been cancelled; the
security no longer exists or is no longer
eligible on the market instructed. For
corporate action related cancellation,
CORP should be used.
OTHR Other Other. See Narrative.
CTHP CancelledByThirdParty Instruction is cancelled by a Third party.
17.1.16.18.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the related instruction is cancelled, or the related cancellation
request is executed.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 409 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 409
   Issuer <Issr> [1..1] Text 409
   SchemeName <SchmeNm> [0..1] Text 409
17.1.16.19  ModificationProcessingStatus9Choice
Definition: Choice of modification processing status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 448
Or}   Proprietary <Prtry> [1..1] ± 449
17.1.16.19.1  Code <Cd>
Presence: [1..1]
Definition: Provides the status of a modification request.
Datatype: "ModificationProcessingStatus1Code" on page 485
CodeName Name Definition
PACK Accepted Modification request has been
acknowledged for further processing by
the account servicer.
REJT Rejected Modification has been rejected for further
processing.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
448 March 2024
```

