---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.3 Constraints"]
file_pages: [215, 216]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
topic_continuations: [{"constraint_ids": ["C20"], "until_heading": "5.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 217, "topic": "5.3 Constraints", "reference_path": "domains/payments/reference/message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00136.md"}]
---

# 5.3 Constraints

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 215 to 216.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 5.3 Constraints topic continues in [Constraints continuation C20 (file p217)](section-00136.md#file-page-217). Read the text before **5.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 215

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or         Code <Cd> [1..1] CodeSet 325
Or}         Proprietary <Prtry> [1..1] Text 325
       Description <Desc> [0..1] Text 325
   SupplementaryData <SplmtryData> [0..*] ± C16 325
5.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C4 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C5 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C6 CreditDebitIndicator1Rule
If PaymentCommonInformation/CreditDebitIndicator is present, then TransactionReport/
Transaction/CreditDebitIndicator is not allowed.
If PaymentCommonInformation/CreditDebitIndicator is not present, then TransactionReport/
Transaction/CreditDebitIndicator is optional.
C7 CreditDebitIndicatorGuideline
The CreditDebitIndicator may be omitted for optimisation reason if the CreditDebitIndicator is
used in the search criteria of the related query.
C8 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 215 February 2025
```

## File page 216

```text
Note: The decimal separator is a dot.
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C10 CurrencyGuideline
The currency may be omitted in the amounts present in the message. However, this should
only be done in cases of one single currency systems (for example, the euro).
This constraint is defined at the MessageDefinition level.
C11 DebitCreditIndicatorGuideline
DebitCreditIndicator should be present when TotalNetEntryAmount is present.
C12 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C13 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C14 IdentificationOrProxyPresenceRule
Identification must be present or proxy must be present.
C15 PaymentInstructionStatusRule
If PaymentCommonInformation/PaymentInstructionStatus is present, then TransactionReport/
Transaction/Payment/InstructionStatus/PaymentInstructionStatus is not allowed.
If PaymentCommonInformation/PaymentInstructionStatus is not present, then
TransactionReport/Transaction/Payment/InstructionStatus/PaymentInstructionStatus is
optional.
C16 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C17 TransactionCreditDebitIndicatorRule
If CreditDebitIndicator is present, then AccountEntry/Entry/Amount or Payment/
InstructedAmount or Payment/InterbankSettlementAmount must be present.
If CreditDebitIndicator is not present, then any Message Elements in the list (AccountEntry/
Entry/Amount, Payment/InstructedAmount, Payment/InterbankSettlementAmount) is optional.
C18 TransactionIdentificationPresenceRule
TransactionIdentification or UETR must be present. Both may be present
C19 TransactionIdentificationPresenceRule
TransactionIdentification or UETR must be present. Both may be present
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 216 February 2025
```

