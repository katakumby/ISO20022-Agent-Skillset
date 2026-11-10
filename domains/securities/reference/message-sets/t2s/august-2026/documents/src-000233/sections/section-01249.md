---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["31 reda.010.001.01 SecurityQueryV01", "31.2 Structure"]
file_pages: [1765, 1766]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.010.001.01"]
---

# 31.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1765 to 1766.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1765

```text
31.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctyQry> [1..1]  C6
   MessageHeader <MsgHdr> [0..1] ± 1767
   RequestType <ReqTp> [0..1] ± 1768
   SearchCriteria <SchCrit> [1..1]  1768
     FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C4, C5,
C7, C8,
C9
1770
     ClassificationFinancialInstrument <ClssfctnFinInstrm> [0..1] IdentifierSet 1771
     MaturityDate <MtrtyDt> [0..1]  1771
{Or       FromDate <FrDt> [1..1] Date 1771
Or       ToDate <ToDt> [1..1] Date 1771
Or       FromToDate <FrToDt> [1..1] ± 1771
Or       EqualDate <EQDt> [1..1] Date 1772
Or}       NotEqualDate <NEQDt> [1..1] Date 1772
     IssueDate <IsseDt> [0..1]  1772
{Or       FromDate <FrDt> [1..1] Date 1772
Or       ToDate <ToDt> [1..1] Date 1772
Or       FromToDate <FrToDt> [1..1] ± 1773
Or       EqualDate <EQDt> [1..1] Date 1773
Or}       NotEqualDate <NEQDt> [1..1] Date 1773
     IssueCurrency <IsseCcy> [0..1] CodeSet C1 1773
     CountryOfIssue <CtryOfIsse> [0..1] CodeSet C3 1773
     SecurityStatus <SctySts> [0..1]  1774
{Or       Code <Cd> [1..1] CodeSet 1774
Or}       Proprietary <Prtry> [1..1] ± 1774
     MaintainingCSD <MntngCSD> [0..1]  1774
{Or       OrganisationIdentification <OrgId> [1..1] ± 1775
Or}       CombinedIdentification <CmbndId> [1..1] ± 1775
     InvestorCSD <InvstrCSD> [0..1]  1775
{Or       OrganisationIdentification <OrgId> [1..1] ± 1775
Or}       CombinedIdentification <CmbndId> [1..1] ± 1776
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.010.001.01 SecurityQueryV01
Target2-Securities 1765 August 2026
```

## File page 1766

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     IssuerCSD <IssrCSD> [0..1]  1776
{Or       OrganisationIdentification <OrgId> [1..1] ± 1776
Or}       CombinedIdentification <CmbndId> [1..1] ± 1776
     TechnicalIssuerCSD <TechIssrCSD> [0..1]  1777
{Or       OrganisationIdentification <OrgId> [1..1] ± 1777
Or}       CombinedIdentification <CmbndId> [1..1] ± 1777
     CSD <CSD> [0..1]  1778
{Or       OrganisationIdentification <OrgId> [1..1] ± 1778
Or}       CombinedIdentification <CmbndId> [1..1] ± 1778
   SmallSetReturnCriteria <SmlSetRtrCrit> [0..1]  1778
     FinancialInstrumentIdentification <FinInstrmId> [1..1] Indicator 1779
     ISOSecurityLongName <ISOSctyLngNm> [1..1] Indicator 1779
     ISOSecurityShortName <ISOSctyShrtNm> [1..1] Indicator 1780
     ClassificationFinancialInstrument <ClssfctnFinInstrm> [1..1] Indicator 1780
     MaturityDate <MtrtyDt> [1..1] Indicator 1780
     IssueDate <IsseDt> [1..1] Indicator 1780
     IssueCurrency <IsseCcy> [1..1] Indicator 1780
     CountryOfIssue <CtryOfIsse> [1..1] Indicator 1780
     SecurityStatus <SctySts> [1..1] Indicator 1781
     InvestorCSD <InvstrCSD> [1..1] Indicator 1781
     IssuerCSD <IssrCSD> [1..1] Indicator 1781
     TechnicalIssuerCSD <TechIssrCSD> [1..1] Indicator 1781
     CSD <CSD> [1..1] Indicator 1781
     SecuritiesQuantityType <SctiesQtyTp> [1..1] Indicator 1782
     MinimumDenomination <MinDnmtn> [1..1] Indicator 1782
     MinimumMultipleQuantity <MinMltplQty> [1..1] Indicator 1782
     DeviatingSettlementUnit <DevtgSttlmUnit> [1..1] Indicator 1782
   SupplementaryData <SplmtryData> [0..*] ± C10 1782
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.010.001.01 SecurityQueryV01
Target2-Securities 1766 August 2026
```

