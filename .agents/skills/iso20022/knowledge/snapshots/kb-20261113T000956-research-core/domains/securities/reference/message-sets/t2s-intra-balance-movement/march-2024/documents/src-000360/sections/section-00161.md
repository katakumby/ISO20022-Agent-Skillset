---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "10.3 Constraints"]
file_pages: [194, 195]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
topic_continuations: [{"constraint_ids": ["C21", "C22", "C23", "C24"], "until_heading": "10.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 196, "topic": "10.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00162.md"}]
---

# 10.3 Constraints

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 194 to 195.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 10.3 Constraints topic continues in [Constraints continuation C21–C24 (file p196)](section-00162.md#file-page-196). Read the text before **10.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 194

```text
10.3 Constraints
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
C3 ActivityIndicatorNoRule
If ReportGeneralDetails/ActivityIndicator is equal to No (false or 0) then ReportOrError must be
absent.
This constraint is defined at the MessageDefinition level.
C4 ActivityIndicatorYesRule
If ReportGeneralDetails/ActivityIndicator is equal to Yes (true or 1) then ReportOrError must be
present.
This constraint is defined at the MessageDefinition level.
C5 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C6 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C7 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C8 CashAccountOwnerRule
CashAccountOwner must be present or Movement(*)/AccountOwner must be present, but not
both.
C9 CashAccountRule
CashAccount must be present or Movement(*)/CashAccount must be present, but not both.
C10 CashAccountServicerRule
CashAccountServicer must be present or Movement(*)/AccountOwner must be present, but not
both.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
194 March 2024
```

## File page 195

```text
C11 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C12 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C13 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C14 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C15 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C16 NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be
NONREF.
C17 PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
C18 QueryTypeFullRule
If ReportGeneralDetails/QueryType is equal to Full, then ReportOrError/Movements(*)/
Movement/MovementDetails must be present.
This constraint is defined at the MessageDefinition level.
C19 QueryTypeStatusRule
If ReportGeneralDetails/QueryType is equal to Status, then ReportOrError/Movements(*)/
Movement/MovementDetails must be absent.
This constraint is defined at the MessageDefinition level.
C20 ReportIdentificationRule
If Long number (Exact5NumericText) is used, then the report must be a delta reports
(UpdateType: DELT).
If the report has multiple pages, then the ReportIdentification must remain the same through all
the pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the
same safekeeping account must have different report identifications. For example, a daily
report sent on day 1 would have ReportIdentification 001, on day 2, 002, etc.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
195 March 2024
```

