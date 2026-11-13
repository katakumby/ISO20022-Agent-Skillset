---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "78.3 Constraints"]
file_pages: [2702, 2703]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.033.001.01"]
topic_continuations: [{"constraint_ids": ["C14", "C15", "C16", "C17", "C18", "C19", "C20", "C21", "C22", "C23"], "until_heading": "78.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 2704, "topic": "78.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-01983.md"}]
---

# 78.3 Constraints

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2702 to 2703.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 78.3 Constraints topic continues in [Constraints continuation C14–C23 (file p2704)](section-01983.md#file-page-2704). Read the text before **78.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 2702

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       Underlying <Undrlyg> [0..1]  2714
{Or         IntraPositionMovement <IntraPosMvmnt> [1..1]  2715
           FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C15
2716
           SettlementQuantity <SttlmQty> [1..1] ± 2717
           SettlementDate <SttlmDt> [1..1] ± 2717
           BalanceFrom <BalFr> [0..1] ± 2717
           BalanceTo <BalTo> [0..1] ± 2718
           SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 2718
           Priority <Prty> [0..1] ± 2718
Or}         SettlementTransaction <SttlmTx> [1..1]  2718
           FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C15
2719
           SettlementQuantity <SttlmQty> [1..1] ± 2720
           SettlementAmount <SttlmAmt> [0..1] ± 2720
           TradeDate <TradDt> [0..1] ± 2721
           SettlementDate <SttlmDt> [1..1] ± 2721
           DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C16,
C17,
C18,
C19
2721
           ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C16,
C17,
C18,
C19
2722
   SupplementaryData <SplmtryData> [0..*] ± C23 2723
78.3 Constraints
C1 AccountOwnerRule
AccountOwner must be present or Cancellation(*)/AccountOwner must be present, but not
both.
C2 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities 2702 August 2026
```

## File page 2703

```text
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C3 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C4 ActivityIndicatorNoRule
If ReportGeneralDetails/ActivityIndicator is equal to No (false or 0) then Cancellations must be
absent.
This constraint is defined at the MessageDefinition level.
C5 ActivityIndicatorYesRule
If ReportGeneralDetails/ActivityIndicator is equal to Yes (true or 1) then Cancellations must be
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities 2703 August 2026
```

