---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.4 Message Building Blocks", "6.4.6 ProtectInstruction <PrtctInstr>", "6.4.6.4 ProtectSafekeepingAccount <PrtctSfkpgAcct>"]
file_pages: [358]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.4.6.4 ProtectSafekeepingAccount <PrtctSfkpgAcct>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 358 to 358.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 358

```text
6.4.6.4  ProtectSafekeepingAccount <PrtctSfkpgAcct>
Presence: [0..1]
Definition: Account which submitted the original protect instruction used for cover protect instructions
whereby one safekeeping account is covering on behalf of another safekeeping account.
Datatype: "Max35Text" on page 1251
6.4.6.5  ProtectDate <PrtctDt>
Presence: [0..1]
Definition: Date at which the protect instruction was created and used for cover protect validation.
Datatype: "ISODate" on page 1243
6.4.6.6  UncoveredProtectQuantity <UcvrdPrtctQty>
Presence: [0..1]
Definition: Remaining quantity of protect instruction which has not been covered.
UncoveredProtectQuantity <UcvrdPrtctQty> contains one of the following elements (see
"FinancialInstrumentQuantity18Choice" on page 1132 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1133
Or}   FaceAmount <FaceAmt> [1..1] Amount 1133
6.4.7 AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information.
AdditionalInformation <AddtlInf> contains the following CorporateActionNarrative10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalText <AddtlTxt> [0..*] Text 358
   PartyContactNarrative <PtyCtctNrrtv> [0..*] Text 358
6.4.7.1  AdditionalText <AddtlTxt>
Presence: [0..*]
Definition: Provides additional information or specifies in more detail the content of a message. This
field may only be used when the information to be transmitted, cannot be coded.
Datatype: "Max350Text" on page 1250
6.4.7.2  PartyContactNarrative <PtyCtctNrrtv>
Presence: [0..*]
Definition: Provides additional information regarding the party, for example, the contact unit or person
responsible for the transaction identified in the message.
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 358 February 2026
```

