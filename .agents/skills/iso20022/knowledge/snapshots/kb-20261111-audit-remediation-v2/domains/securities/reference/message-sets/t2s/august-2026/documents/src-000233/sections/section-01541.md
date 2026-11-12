---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["44 reda.024.001.01 CollateralValueCreationRequestV01", "44.2 Structure"]
file_pages: [2164]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.024.001.01"]
---

# 44.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2164 to 2164.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2164

```text
44.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CollValCreReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2166
   CollateralValue <CollVal> [1..*]  2166
     SecurityIdentification <SctyId> [1..1] ± C7, C8,
C9, C10,
C11
2167
     ValuationDate <ValtnDt> [1..1] Date 2168
     ValuationCurrency <ValtnCcy> [0..1] CodeSet C1 2168
     ValuationPrice <ValtnPric> [1..1]  2168
{Or       Amount <Amt> [1..1] Amount 2168
Or       AmountWithCurrency <AmtWthCcy> [1..1] Amount C2, C5 2168
Or}       Coefficient <Coeff> [1..1] Quantity 2169
     ValuationCloseLinkPrice <ValtnClsLkPric> [0..1]  2169
{Or       Amount <Amt> [1..1] Amount 2169
Or       AmountWithCurrency <AmtWthCcy> [1..1] Amount C2, C5 2169
Or}       Coefficient <Coeff> [1..1] Quantity 2170
     CleanPrice <CleanPric> [0..1] ± 2170
     AccruedInterest <AcrdIntrst> [0..1] ± 2170
     Haircut <Hrcut> [0..1] Rate 2170
     CloseLinkHaircut <ClsLkHrcut> [0..1] Rate 2171
     PoolFactor <PoolFctr> [0..1] Rate 2171
     ForeignExchange <FX> [0..1] ± 2171
   PartyIdentification <PtyId> [1..1]  2171
{Or     OrganisationIdentification <OrgId> [1..1] ± 2171
Or}     CombinedIdentification <CmbndId> [1..1] ± 2172
   SupplementaryData <SplmtryData> [0..*] ± C12 2172
44.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.024.001.01
CollateralValueCreationRequestV01
Target2-Securities 2164 August 2026
```

