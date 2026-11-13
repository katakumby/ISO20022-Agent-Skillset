---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 reda.015.001.01 PartyQueryV01", "3.2 Structure"]
file_pages: [19, 20]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.015.001.01"]
---

# 3.2 Structure

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 19 to 20.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 19

```text
3.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PtyQry> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 21
   SearchCriteria <SchCrit> [1..1]  21
     OpeningDate <OpngDt> [0..1]  23
{Or       FromDate <FrDt> [1..1] Date 23
Or       ToDate <ToDt> [1..1] Date 23
Or       FromToDate <FrToDt> [1..1] ± 23
Or       EqualDate <EQDt> [1..1] Date 24
Or}       NotEqualDate <NEQDt> [1..1] Date 24
     ClosingDate <ClsgDt> [0..1]  24
{Or       FromDate <FrDt> [1..1] Date 24
Or       ToDate <ToDt> [1..1] Date 24
Or       FromToDate <FrToDt> [1..1] ± 24
Or       EqualDate <EQDt> [1..1] Date 25
Or}       NotEqualDate <NEQDt> [1..1] Date 25
     Type <Tp> [0..1]  25
{Or       Code <Cd> [1..1] CodeSet 25
Or}       Proprietary <Prtry> [1..1] Text 25
     ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 25
     PartyIdentification <PtyId> [0..1] ± 26
     RestrictionIdentification <RstrctnId> [0..1] Text 26
     RestrictionIssueDate <RstrctnIsseDt> [0..1]  26
{Or       DateTime <DtTm> [1..1]  27
{Or         FromDateTime <FrDtTm> [1..1] DateTime 27
Or         ToDateTime <ToDtTm> [1..1] DateTime 27
Or         FromToDateTime <FrToDtTm> [1..1] ± 28
Or         EqualDateTime <EQDtTm> [1..1] DateTime 28
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 28
Or}       Date <Dt> [1..1]  28
{Or         FromDate <FrDt> [1..1] Date 28
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.015.001.01 PartyQueryV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
19 March 2024
```

## File page 20

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or         ToDate <ToDt> [1..1] Date 28
Or         FromToDate <FrToDt> [1..1] ± 29
Or         EqualDate <EQDt> [1..1] Date 29
Or}         NotEqualDate <NEQDt> [1..1] Date 29
     ResidenceType <ResTp> [0..1] CodeSet 29
     LockStatus <LckSts> [0..1]  29
       ValidFrom <VldFr> [0..1] Date 30
       Status <Sts> [1..1] CodeSet 30
       LockReason <LckRsn> [0..*] Text 30
   ReturnCriteria <RtrCrit> [0..1]  30
     OpeningDate <OpngDt> [0..1] Indicator 31
     ClosingDate <ClsgDt> [0..1] Indicator 31
     Type <Tp> [0..1] Indicator 31
     PartyIdentification <PtyId> [0..1] Indicator 32
     ResponsiblePartyIdentification <RspnsblPtyId> [0..1] Indicator 32
     RestrictionIdentification <RstrctnId> [0..1] Indicator 32
     RestrictedOnDate <RstrctdOnDt> [0..1] Indicator 32
     Name <Nm> [0..1] Indicator 32
     ShortName <ShrtNm> [0..1] Indicator 33
     Address <Adr> [0..1] Indicator 33
     TechnicalAddress <TechAdr> [0..1] Indicator 33
     ContactDetails <CtctDtls> [0..1] Indicator 33
     ResidenceType <ResTp> [0..1] Indicator 33
     LockStatus <LckSts> [0..1] Indicator 34
     MarketSpecificAttribute <MktSpcfcAttr> [0..1] Indicator 34
   SupplementaryData <SplmtryData> [0..*] ± C3 34
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.015.001.01 PartyQueryV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
20 March 2024
```

