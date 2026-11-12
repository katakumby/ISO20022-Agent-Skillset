---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15", "13.4 Message Building Blocks", "13.4.6 ProtectInstruction <PrtctInstr>", "13.4.6.5 UncoveredProtectQuantity <UcvrdPrtctQty>"]
file_pages: [755, 756]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.041.001.15"]
---

# 13.4.6.5 UncoveredProtectQuantity <UcvrdPrtctQty>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 755 to 756.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 755

```text
13.4.6.5  UncoveredProtectQuantity <UcvrdPrtctQty>
Presence: [0..1]
Definition: Remaining quantity of protect instruction which has not been covered.
UncoveredProtectQuantity <UcvrdPrtctQty> contains one of the following elements (see
"FinancialInstrumentQuantity18Choice" on page 1132 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1133
Or}   FaceAmount <FaceAmt> [1..1] Amount 1133
13.4.7 AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information.
AdditionalInformation <AddtlInf> contains the following CorporateActionNarrative10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalText <AddtlTxt> [0..*] Text 755
   PartyContactNarrative <PtyCtctNrrtv> [0..*] Text 755
13.4.7.1  AdditionalText <AddtlTxt>
Presence: [0..*]
Definition: Provides additional information or specifies in more detail the content of a message. This
field may only be used when the information to be transmitted, cannot be coded.
Datatype: "Max350Text" on page 1250
13.4.7.2  PartyContactNarrative <PtyCtctNrrtv>
Presence: [0..*]
Definition: Provides additional information regarding the party, for example, the contact unit or person
responsible for the transaction identified in the message.
Datatype: "Max350Text" on page 1250
13.4.8 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C29 "SupplementaryDataRule"
Approved by the Securities SEG on 27 January 2026 seev.041.001.15
CorporateActionInstructionCancellationRequestStat
usAdviceV15
Corporate Actions - Maintenance 2025 - 2026 755 February 2026
```

## File page 756

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 924 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 924
   Envelope <Envlp> [1..1] (External Schema) 924
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 27 January 2026 seev.041.001.15
CorporateActionInstructionCancellationRequestStat
usAdviceV15
Corporate Actions - Maintenance 2025 - 2026 756 February 2026
```

