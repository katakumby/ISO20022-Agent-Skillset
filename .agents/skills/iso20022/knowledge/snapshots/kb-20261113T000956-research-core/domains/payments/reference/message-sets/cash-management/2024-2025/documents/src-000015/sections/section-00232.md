---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 camt.008.001.11 CancelTransactionV11", "7.3 Constraints"]
file_pages: [350]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.008.001.11"]
topic_continuations: [{"constraint_ids": ["C10"], "until_heading": "7.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 351, "topic": "7.3 Constraints", "reference_path": "domains/payments/reference/message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00233.md"}]
---

# 7.3 Constraints

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 350 to 350.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 7.3 Constraints topic continues in [Constraints continuation C10 (file p351)](section-00233.md#file-page-351). Read the text before **7.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 350

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     Originator <Orgtr> [0..1] ± 361
     Reason <Rsn> [0..1] ± 362
     AdditionalInformation <AddtlInf> [0..*] Text 363
   SupplementaryData <SplmtryData> [0..*] ± C8 363
7.3 Constraints
C1 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C2 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C3 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C4 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C5 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C6 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C7 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C8 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C9 TransactionIdentificationPresenceRule
TransactionIdentification or UETR must be present. Both may be present
Approved by the Payments SEG on 04 February 2025 camt.008.001.11 CancelTransactionV11
Cash Management - Maintenance 2024 - 2025 350 February 2025
```

