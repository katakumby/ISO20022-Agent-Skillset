---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["6 reda.010.001.01 SecurityQueryV01", "6.3 Constraints"]
file_pages: [79]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.010.001.01"]
---

# 6.3 Constraints

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 79 to 79.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 79

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     FinancialInstrumentIdentification <FinInstrmId> [1..1] Indicator 89
     ISOSecurityLongName <ISOSctyLngNm> [1..1] Indicator 89
     ISOSecurityShortName <ISOSctyShrtNm> [1..1] Indicator 90
     ClassificationFinancialInstrument <ClssfctnFinInstrm> [1..1] Indicator 90
     MaturityDate <MtrtyDt> [1..1] Indicator 90
     IssueDate <IsseDt> [1..1] Indicator 90
     IssueCurrency <IsseCcy> [1..1] Indicator 90
     CountryOfIssue <CtryOfIsse> [1..1] Indicator 90
     SecurityStatus <SctySts> [1..1] Indicator 91
     InvestorCSD <InvstrCSD> [1..1] Indicator 91
     IssuerCSD <IssrCSD> [1..1] Indicator 91
     TechnicalIssuerCSD <TechIssrCSD> [1..1] Indicator 91
     CSD <CSD> [1..1] Indicator 91
     SecuritiesQuantityType <SctiesQtyTp> [1..1] Indicator 92
     MinimumDenomination <MinDnmtn> [1..1] Indicator 92
     MinimumMultipleQuantity <MinMltplQty> [1..1] Indicator 92
     DeviatingSettlementUnit <DevtgSttlmUnit> [1..1] Indicator 92
   SupplementaryData <SplmtryData> [0..*] ± C10 92
6.3 Constraints
C1 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C2 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C3 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C4 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.010.001.01 SecurityQueryV01
Target2-Securities - Securities Reference Data 79 March 2024
```

