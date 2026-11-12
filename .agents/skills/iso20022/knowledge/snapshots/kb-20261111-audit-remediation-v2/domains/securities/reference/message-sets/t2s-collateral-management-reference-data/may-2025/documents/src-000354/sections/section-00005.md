---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["2 reda.024.001.01 CollateralValueCreationRequestV01", "2.2 Structure"]
file_pages: [7]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.024.001.01"]
---

# 2.2 Structure

Source: [src-000354](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 7 to 7.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 7

```text
2.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CollValCreReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 9
   CollateralValue <CollVal> [1..*]  9
     SecurityIdentification <SctyId> [1..1] ± C7, C8,
C9, C10,
C11
10
     ValuationDate <ValtnDt> [1..1] Date 11
     ValuationCurrency <ValtnCcy> [0..1] CodeSet C1 11
     ValuationPrice <ValtnPric> [1..1]  11
{Or       Amount <Amt> [1..1] Amount 11
Or       AmountWithCurrency <AmtWthCcy> [1..1] Amount C2, C5 11
Or}       Coefficient <Coeff> [1..1] Quantity 12
     ValuationCloseLinkPrice <ValtnClsLkPric> [0..1]  12
{Or       Amount <Amt> [1..1] Amount 12
Or       AmountWithCurrency <AmtWthCcy> [1..1] Amount C2, C5 12
Or}       Coefficient <Coeff> [1..1] Quantity 13
     CleanPrice <CleanPric> [0..1] ± 13
     AccruedInterest <AcrdIntrst> [0..1] ± 13
     Haircut <Hrcut> [0..1] Rate 13
     CloseLinkHaircut <ClsLkHrcut> [0..1] Rate 14
     PoolFactor <PoolFctr> [0..1] Rate 14
     ForeignExchange <FX> [0..1] ± 14
   PartyIdentification <PtyId> [1..1]  14
{Or     OrganisationIdentification <OrgId> [1..1] ± 14
Or}     CombinedIdentification <CmbndId> [1..1] ± 15
   SupplementaryData <SplmtryData> [0..*] ± C12 15
2.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
Approved by the Securities SEG on 17 April 2025. reda.024.001.01
CollateralValueCreationRequestV01
Target2-Securities - Collateral Management Reference Data 7 May 2025
```

