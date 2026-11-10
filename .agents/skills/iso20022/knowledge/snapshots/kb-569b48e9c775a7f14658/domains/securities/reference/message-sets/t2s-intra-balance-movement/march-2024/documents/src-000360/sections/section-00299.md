---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["16 camt.085.001.02 IntraBalanceMovementPendingReportV02", "16.3 Constraints"]
file_pages: [361, 362]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.085.001.02"]
---

# 16.3 Constraints

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 361 to 362.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 361

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or           MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 384
Or           PoolIdentification <PoolId> [1..1] Text 384
Or}           OtherTransactionIdentification <OthrTxId> [1..1] Text 384
         ReferenceOwner <RefOwnr> [0..1] ± 384
       Priority <Prty> [0..1] ± 385
       MessageOriginator <MsgOrgtr> [0..1] ± 385
       CreationDateTime <CreDtTm> [1..1] DateTime 385
       InstructionProcessingAdditionalDetails <InstrPrcgAddtlDtls> [0..1] Text 385
       SupplementaryData <SplmtryData> [0..*] ± C18 385
16.3 Constraints
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
If ReportGeneralDetails/ActivityIndicator is equal to No (false or 0) then Movements must be
absent.
This constraint is defined at the MessageDefinition level.
C4 ActivityIndicatorYesRule
If ReportGeneralDetails/ActivityIndicator is equal to Yes (true or 1) then Movements must be
present.
This constraint is defined at the MessageDefinition level.
C5 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C6 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
361 March 2024
```

## File page 362

```text
C7 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C8 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C10 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C11 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C12 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C13 NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be
NONREF.
C14 PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
C15 ReportNumberRule
If Long number (Exact5NumericTest) is used, then the report must be a delta reports
(UpdateType: DELT).
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the
same safekeeping account must have different ReportNumbers. For example, a daily report
sent on day 1 would have ReportNumber 001, on day 2, 002, etc.
C16 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C17 StatusAndReasonRule
StatusAndReason must be present or Movement(*)/StatusAndReason must be present, but not
both.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
362 March 2024
```

