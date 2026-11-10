---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.4 Message Building Blocks", "6.4.4 InstructionProcessingStatus <InstrPrcgSts>", "6.4.4.6 Returned <Rtrd>", "6.4.4.6.2 ReturnedReason <RtrdRsn>", "6.4.4.6.2.2 Reason <Rsn>", "6.4.4.6.2.2.1 ReasonCode <RsnCd>", "6.4.4.6.2.2.1.1 Code <Cd>"]
file_pages: [347]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.4.4.6.2.2.1.1 Code <Cd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 347 to 347.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 347

```text
ReasonCode <RsnCd> contains one of the following ReturnedReason2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 347
Or}   Proprietary <Prtry> [1..1] ± 347
6.4.4.6.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Returned reason specified as a code.
Datatype: "ReturnedStatus1Code" on page 1241
CodeName Name Definition
NARR NarrativeReason See narrative field for reason.
PROR Prorated Shares returned due to prorated
acceptance.
6.4.4.6.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Returned reason specified as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
6.4.4.6.2.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Additional information about the returned status.
Datatype: "Max210Text" on page 1249
6.4.4.7  DefaultAction <DfltActn>
Presence: [1..1]
Definition: Default action is taken.
DefaultAction <DfltActn> contains the following elements (see "NoSpecifiedReason1" on page 1144 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1144
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 347 February 2026
```

