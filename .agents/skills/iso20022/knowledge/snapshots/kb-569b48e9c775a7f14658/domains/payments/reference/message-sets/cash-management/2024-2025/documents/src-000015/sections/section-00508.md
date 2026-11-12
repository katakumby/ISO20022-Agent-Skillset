---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["28 camt.050.001.07 LiquidityCreditTransferV07", "28.4 Message Building Blocks"]
file_pages: [670]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.050.001.07"]
---

# 28.4 Message Building Blocks

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 670 to 670.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 670

```text
C5 CreditAccountRule
At least CreditAccount or Creditor must be present, or both.
C6 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C7 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C8 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C9 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C10 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
28.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
28.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 811 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 812
   CreationDateTime <CreDtTm> [0..1] DateTime 812
28.4.2 LiquidityCreditTransfer <LqdtyCdtTrf>
Presence: [1..1]
Definition: Details of the liquidity credit transfer.
Impacted by: C5 "CreditAccountRule"
Approved by the Payments SEG on 04 February 2025 camt.050.001.07 LiquidityCreditTransferV07
Cash Management - Maintenance 2024 - 2025 670 February 2025
```

