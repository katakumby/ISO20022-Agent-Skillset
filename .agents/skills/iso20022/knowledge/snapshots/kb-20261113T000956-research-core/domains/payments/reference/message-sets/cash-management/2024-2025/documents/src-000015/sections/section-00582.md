---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["34 camt.102.001.03 CreateStandingOrderV03", "34.4 Message Building Blocks"]
file_pages: [757]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.102.001.03"]
---

# 34.4 Message Building Blocks

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 757 to 757.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 757

```text
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C4 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C5 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C6 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C7 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C8 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C9 ModifyStandingOrderValueSetRule
At least one element must be present.
C10 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
34.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
34.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Common business identification for the message.
Approved by the Payments SEG on 04 February 2025 camt.102.001.03 CreateStandingOrderV03
Cash Management - Maintenance 2024 - 2025 757 February 2025
```

