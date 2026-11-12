---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["33 camt.101.001.02 CreateLimitV02", "33.4 Message Building Blocks"]
file_pages: [747]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.101.001.02"]
---

# 33.4 Message Building Blocks

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 747 to 747.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 747

```text
C6 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C7 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C8 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
33.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
33.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 811 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 812
   CreationDateTime <CreDtTm> [0..1] DateTime 812
33.4.2 LimitData <LmtData>
Presence: [1..*]
Definition: Identifies one particular limit set by the member and managed by the transaction
administrator.
Approved by the Payments SEG on 04 February 2025 camt.101.001.02 CreateLimitV02
Cash Management - Maintenance 2024 - 2025 747 February 2025
```

