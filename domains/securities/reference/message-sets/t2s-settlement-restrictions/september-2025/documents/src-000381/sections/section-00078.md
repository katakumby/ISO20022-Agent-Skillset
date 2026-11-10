---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "5.3 Constraints"]
file_pages: [100, 101, 102]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 5.3 Constraints

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 100 to 102.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 100

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C16
126
           SettlementQuantity <SttlmQty> [1..1] ± 127
           SettlementDate <SttlmDt> [1..1] ± 127
           BalanceFrom <BalFr> [0..1] ± 127
           BalanceTo <BalTo> [0..1] ± 128
           SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 128
           Priority <Prty> [0..1] ± 128
Or}         SettlementTransaction <SttlmTx> [1..1]  128
           FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C16
129
           SettlementQuantity <SttlmQty> [1..1] ± 130
           SettlementAmount <SttlmAmt> [0..1] ± 130
           TradeDate <TradDt> [0..1] ± 131
           SettlementDate <SttlmDt> [1..1] ± 131
           DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C18,
C19,
C20,
C21
131
           ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C18,
C19,
C20,
C21
132
   SupplementaryData <SplmtryData> [0..*] ± C28 133
5.3 Constraints
C1 AccountOwnerRule
AccountOwner must be present or Modification(*)/AccountOwner must be present, but not both.
C2 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 100 September 2025
```

## File page 101

```text
C3 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C4 ActivityIndicatorNoRule
If ReportGeneralDetails/ActivityIndicator is equal to No (false or 0) then Modifications must be
absent.
This constraint is defined at the MessageDefinition level.
C5 ActivityIndicatorYesRule
If ReportGeneralDetails/ActivityIndicator is equal to Yes (true or 1) then Modifications must be
present.
This constraint is defined at the MessageDefinition level.
C6 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C7 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C8 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C10 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C11 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C12 DescriptionUsageRule
Description must be used alone as the last resort.
C13 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 101 September 2025
```

## File page 102

```text
C14 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C15 ModificationRequestPresenceRule
At least one securities settlement conditions modification request type must be present.
C16 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C17 OtherProcessingRule
If OtherProcessing is used, then its usage must be pre-agreed between the sender and
receiver.
C18 Party2PresenceRule
If Party2 is present, then Party1 must be present.
C19 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C20 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C21 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C22 ProcessingStatusRule
ProcessingStatus must be present or Modification(*)/ProcessingStatus must be present, but not
both.
C23 ReferencePresenceRule
At least one reference must be present.
C24 ReportNumberRule
If Long number (Exact5NumericTest) is used, then the report must be a delta reports
(UpdateType: DELT).
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the
same safekeeping account must have different ReportNumbers. For example, a daily report
sent on day 1 would have ReportNumber 001, on day 2, 002, etc.
C25 SafekeepingAccountRule
SafekeepingAccount must be present or Modification(*)/SafekeepingAccount must be present,
but not both.
C26 SettlementConditionModificationApplicabilityRule
All settlement condition modification request types do not apply to all account servicers.
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 102 September 2025
```

