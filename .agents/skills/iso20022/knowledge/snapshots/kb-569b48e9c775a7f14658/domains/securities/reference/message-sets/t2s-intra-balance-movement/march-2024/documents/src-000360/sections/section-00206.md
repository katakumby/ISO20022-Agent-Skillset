---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["12 camt.081.001.02 IntraBalanceMovementModificationReportV02", "12.3 Constraints"]
file_pages: [249, 250]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.081.001.02"]
---

# 12.3 Constraints

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 249 to 250.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 249

```text
12.3 Constraints
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
C5 AdditionalDetailsRule
Unless bilaterally agreed between the sender and the receiver, if
InstructionProcessingAdditionalDetails is present, then it must not contain information that can
be provided in a structured field.
C6 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C7 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C8 BalanceFromToRule
The cash balance type of BalanceFrom must be different from the cash balance type of
BalanceTo.
C9 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C10 CashAccountOwnerRule
CashAccountOwner must be present or Cancellation(*)/AccountOwner must be present, but not
both.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
249 March 2024
```

## File page 250

```text
C11 CashAccountRule
CashAccount must be present or Cancellation(*)/CashAccount must be present, but not both.
C12 CashAccountServicerRule
CashAccountServicer must be present or Cancellation(*)/AccountOwner must be present, but
not both.
C13 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C14 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C15 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C16 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C17 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C18 ModificationRequestPresenceRule
At least one modification request type element must be present.
C19 OtherProcessingRule
If OtherProcessing is used, then its usage must be pre-agreed between the sender and the
receiver.
C20 ProcessingStatusRule
ProcessingStatus must be present or Cancellation(*)/ProcessingStatus must be present, but
not both.
C21 QueryTypeFullRule
If ReportGeneralDetails/QueryType is equal to Full, then ReportOrError/Modifications(*)/
Modification/UnderlyingIntraBalance must be present.
This constraint is defined at the MessageDefinition level.
C22 QueryTypeStatusRule
If ReportGeneralDetails/QueryType is equal to Status, then ReportOrError/Modifications(*)/
Modification/UnderlyingIntraBalance must be absent.
This constraint is defined at the MessageDefinition level.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
250 March 2024
```

