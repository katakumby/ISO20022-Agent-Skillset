---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["37 reda.017.001.02 PartyReportV02", "37.2 Structure"]
file_pages: [2079]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.017.001.02"]
---

# 37.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2079 to 2079.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2079

```text
37.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PtyRpt> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2081
   ReportOrError <RptOrErr> [1..1]  2081
{Or     PartyReport <PtyRpt> [1..*]  2083
       PartyIdentification <PtyId> [1..1] ± 2085
       PartyOrError <PtyOrErr> [1..1]  2085
{Or         SystemParty <SysPty> [1..1]  2087
           PartyIdentification <PtyId> [0..1]  2089
             Identification <Id> [1..1] ± 2089
             ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 2089
             ValidFrom <VldFr> [0..1] Date 2089
           Address <Adr> [0..1] ± 2089
           ContactDetails <CtctDtls> [0..*] ± 2090
           OpeningDate <OpngDt> [0..1] Date 2091
           ClosingDate <ClsgDt> [0..1] Date 2091
           Type <Tp> [0..1]  2091
{Or             Code <Cd> [1..1] CodeSet 2092
Or}             Proprietary <Prtry> [1..1] Text 2092
           TechnicalAddress <TechAdr> [0..*]  2092
{Or             BICFI <BICFI> [1..1] IdentifierSet C2 2092
Or}             TechnicalAddress <TechAdr> [1..1] Text 2092
           MarketSpecificAttribute <MktSpcfcAttr> [0..*]  2093
             Name <Nm> [1..1] Text 2093
             Value <Val> [1..1] Text 2093
           Name <Nm> [0..1]  2093
             ValidFrom <VldFr> [0..1] Date 2093
             Name <Nm> [1..1] Text 2093
             ShortName <ShrtNm> [0..1] Text 2093
           ResidenceType <ResTp> [0..1] CodeSet 2094
           LockStatus <LckSts> [0..1]  2094
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.017.001.02 PartyReportV02
Target2-Securities 2079 August 2026
```

