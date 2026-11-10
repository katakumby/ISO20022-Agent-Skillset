---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.16 Status", "17.1.16.6 AcknowledgementReason12Choice", "17.1.16.6.2 Proprietary <Prtry>"]
file_pages: [433]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.16.6.2 Proprietary <Prtry>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 433 to 433.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 433

```text
CodeName Name Definition
published for the concerned market or
process.
OTHR Other Other. See Narrative.
CDCY ConditionalCurrency Execution is conditional to the execution
of a process linked to the currency of the
transaction.
CDRG ConditionalRegistrar Execution is conditional to the execution
of a process at the registrar.
CDRE ConditionalRealignement Execution is conditional to the execution
of a process of realignment at the issuer
CSD.
NSTP NotStraightThroughProcessing Instruction was not straight through
processing and had to be processed
manually.
RQWV AcceptedWithoutVotingRights Instruction registration is accepted but
the registration is not in full, that is, not
with voting rights.
LATE MarketDeadlineMissed Instruction was received after market
deadline.
17.1.16.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies additional information about the processed instruction.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 409 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 409
   Issuer <Issr> [1..1] Text 409
   SchemeName <SchmeNm> [0..1] Text 409
17.1.16.7  DeniedReason16Choice
Definition: Choice of format for the denied reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 433
Or}   Proprietary <Prtry> [1..1] ± 434
17.1.16.7.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the request was denied.
Datatype: "DeniedReason4Code" on page 478
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
433 March 2024
```

