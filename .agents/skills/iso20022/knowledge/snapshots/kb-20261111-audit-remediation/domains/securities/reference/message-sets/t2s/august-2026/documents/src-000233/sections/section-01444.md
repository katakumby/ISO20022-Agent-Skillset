---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["35 reda.015.001.01 PartyQueryV01", "35.2 Structure"]
file_pages: [2056, 2057]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.015.001.01"]
---

# 35.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2056 to 2057.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2056

```text
35.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PtyQry> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2058
   SearchCriteria <SchCrit> [1..1]  2058
     OpeningDate <OpngDt> [0..1]  2060
{Or       FromDate <FrDt> [1..1] Date 2060
Or       ToDate <ToDt> [1..1] Date 2060
Or       FromToDate <FrToDt> [1..1] ± 2060
Or       EqualDate <EQDt> [1..1] Date 2061
Or}       NotEqualDate <NEQDt> [1..1] Date 2061
     ClosingDate <ClsgDt> [0..1]  2061
{Or       FromDate <FrDt> [1..1] Date 2061
Or       ToDate <ToDt> [1..1] Date 2061
Or       FromToDate <FrToDt> [1..1] ± 2061
Or       EqualDate <EQDt> [1..1] Date 2062
Or}       NotEqualDate <NEQDt> [1..1] Date 2062
     Type <Tp> [0..1]  2062
{Or       Code <Cd> [1..1] CodeSet 2062
Or}       Proprietary <Prtry> [1..1] Text 2062
     ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 2062
     PartyIdentification <PtyId> [0..1] ± 2063
     RestrictionIdentification <RstrctnId> [0..1] Text 2063
     RestrictionIssueDate <RstrctnIsseDt> [0..1]  2063
{Or       DateTime <DtTm> [1..1]  2064
{Or         FromDateTime <FrDtTm> [1..1] DateTime 2064
Or         ToDateTime <ToDtTm> [1..1] DateTime 2064
Or         FromToDateTime <FrToDtTm> [1..1] ± 2065
Or         EqualDateTime <EQDtTm> [1..1] DateTime 2065
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 2065
Or}       Date <Dt> [1..1]  2065
{Or         FromDate <FrDt> [1..1] Date 2065
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.015.001.01 PartyQueryV01
Target2-Securities 2056 August 2026
```

## File page 2057

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or         ToDate <ToDt> [1..1] Date 2065
Or         FromToDate <FrToDt> [1..1] ± 2066
Or         EqualDate <EQDt> [1..1] Date 2066
Or}         NotEqualDate <NEQDt> [1..1] Date 2066
     ResidenceType <ResTp> [0..1] CodeSet 2066
     LockStatus <LckSts> [0..1]  2066
       ValidFrom <VldFr> [0..1] Date 2067
       Status <Sts> [1..1] CodeSet 2067
       LockReason <LckRsn> [0..*] Text 2067
   ReturnCriteria <RtrCrit> [0..1]  2067
     OpeningDate <OpngDt> [0..1] Indicator 2068
     ClosingDate <ClsgDt> [0..1] Indicator 2068
     Type <Tp> [0..1] Indicator 2068
     PartyIdentification <PtyId> [0..1] Indicator 2069
     ResponsiblePartyIdentification <RspnsblPtyId> [0..1] Indicator 2069
     RestrictionIdentification <RstrctnId> [0..1] Indicator 2069
     RestrictedOnDate <RstrctdOnDt> [0..1] Indicator 2069
     Name <Nm> [0..1] Indicator 2069
     ShortName <ShrtNm> [0..1] Indicator 2070
     Address <Adr> [0..1] Indicator 2070
     TechnicalAddress <TechAdr> [0..1] Indicator 2070
     ContactDetails <CtctDtls> [0..1] Indicator 2070
     ResidenceType <ResTp> [0..1] Indicator 2070
     LockStatus <LckSts> [0..1] Indicator 2071
     MarketSpecificAttribute <MktSpcfcAttr> [0..1] Indicator 2071
   SupplementaryData <SplmtryData> [0..*] ± C3 2071
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.015.001.01 PartyQueryV01
Target2-Securities 2057 August 2026
```

