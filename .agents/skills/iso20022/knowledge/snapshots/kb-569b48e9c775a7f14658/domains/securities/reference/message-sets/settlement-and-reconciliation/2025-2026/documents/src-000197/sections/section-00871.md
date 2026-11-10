---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08", "33.3 Constraints"]
file_pages: [1303, 1304]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.039.001.08"]
---

# 33.3 Constraints

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1303 to 1304.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1303

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C9, C10,
C12,
C13,
C15
1316
       ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 1317
       CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  1317
{Or         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1317
Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1318
Or}         LEI <LEI> [1..1] IdentifierSet 1318
     SettlementDate <SttlmDt> [1..1] ± 1318
     TradeDate <TradDt> [0..1] ± 1318
     DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C16,
C17,
C18,
C19
1319
     ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C16,
C17,
C18,
C19
1320
     Investor <Invstr> [0..1] ± 1321
   SupplementaryData <SplmtryData> [0..*] ± C25 1321
33.3 Constraints
C1 AccountOwnerTransactionIdentificationRule
If AccountOwnerTransactionIdentification is NONREF then at least one of the other references
must be present.
C2 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C3 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C4 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
Approved by the Securities SEG on 27 January 2026 sese.039.001.08
SecuritiesSettlementTransactionModificationReques
tStatusAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 1303 March 2026
```

## File page 1304

```text
C5 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C6 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C7 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C8 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C9 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C10 DescriptionUsageRule
Description must be used alone as the last resort.
C11 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C12 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C13 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C14 NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, then the
AccountOwnerTransactionIdentification must be NONREF.
C15 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C16 Party2PresenceRule
If Party2 is present, then Party1 must be present.
C17 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C18 Party4PresenceRule
If Party4 is present, then Party3 must be present.
Approved by the Securities SEG on 27 January 2026 sese.039.001.08
SecuritiesSettlementTransactionModificationReques
tStatusAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 1304 March 2026
```

