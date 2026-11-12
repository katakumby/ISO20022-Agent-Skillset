---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["19 camt.081.001.02 IntraBalanceMovementModificationReportV02", "19.3 Constraints"]
file_pages: [440, 441]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.081.001.02"]
topic_continuations: [{"constraint_ids": ["C23", "C24", "C25", "C26"], "until_heading": "19.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 442, "topic": "19.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00342.md"}]
---

# 19.3 Constraints

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 440 to 441.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 19.3 Constraints topic continues in [Constraints continuation C23–C26 (file p442)](section-00342.md#file-page-442). Read the text before **19.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 440

```text
19.3 Constraints
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities 440 August 2026
```

## File page 441

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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities 441 August 2026
```

