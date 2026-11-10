---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["58 reda.041.001.02 PartyActivityAdviceV02", "58.2 Structure"]
file_pages: [2257, 2258]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.041.001.02"]
---

# 58.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2257 to 2258.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2257

```text
58.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PtyActvtyAdvc> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2260
   PartyActivity <PtyActvty> [1..1]  2260
     SystemDate <SysDt> [1..1] Date 2263
     Change <Chng> [0..*]  2263
       PartyIdentification <PtyId> [1..1] ± 2266
       Record <Rcrd> [1..*]  2266
{Or         Address <Adr> [1..1]  2269
           Old <Od> [1..1] ± 2269
           New <New> [1..1] ± 2270
Or         ContactDetails <CtctDtls> [1..1]  2271
           Old <Od> [1..1] ± 2271
           New <New> [1..1] ± 2272
Or         OpeningDate <OpngDt> [1..1]  2273
           Old <Od> [1..1] Date 2273
           New <New> [1..1] Date 2273
Or         ClosingDate <ClsgDt> [1..1]  2274
           Old <Od> [1..1] Date 2274
           New <New> [1..1] Date 2274
Or         Type <Tp> [1..1]  2274
           Old <Od> [1..1]  2274
{Or             Code <Cd> [1..1] CodeSet 2275
Or}             Proprietary <Prtry> [1..1] Text 2275
           New <New> [1..1]  2275
{Or             Code <Cd> [1..1] CodeSet 2275
Or}             Proprietary <Prtry> [1..1] Text 2275
Or         TechnicalAddress <TechAdr> [1..1]  2275
           Old <Od> [1..1]  2276
{Or             BICFI <BICFI> [1..1] IdentifierSet C2 2276
Or}             TechnicalAddress <TechAdr> [1..1] Text 2276
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities 2257 August 2026
```

## File page 2258

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           New <New> [1..1]  2276
{Or             BICFI <BICFI> [1..1] IdentifierSet C2 2277
Or}             TechnicalAddress <TechAdr> [1..1] Text 2277
Or         MarketSpecificAttribute <MktSpcfcAttr> [1..1]  2277
           Old <Od> [1..1]  2277
             Name <Nm> [1..1] Text 2278
             Value <Val> [1..1] Text 2278
           New <New> [1..1]  2278
             Name <Nm> [1..1] Text 2278
             Value <Val> [1..1] Text 2278
Or         Name <Nm> [1..1]  2278
           Old <Od> [1..1]  2279
             ValidFrom <VldFr> [0..1] Date 2279
             Name <Nm> [1..1] Text 2279
             ShortName <ShrtNm> [0..1] Text 2279
           New <New> [1..1]  2279
             ValidFrom <VldFr> [0..1] Date 2280
             Name <Nm> [1..1] Text 2280
             ShortName <ShrtNm> [0..1] Text 2280
Or         ResidenceType <ResTp> [1..1]  2280
           Old <Od> [1..1] CodeSet 2280
           New <New> [1..1] CodeSet 2281
Or         LockStatus <LckSts> [1..1]  2281
           Old <Od> [1..1]  2281
             ValidFrom <VldFr> [0..1] Date 2282
             Status <Sts> [1..1] CodeSet 2282
             LockReason <LckRsn> [0..*] Text 2282
           New <New> [1..1]  2282
             ValidFrom <VldFr> [0..1] Date 2282
             Status <Sts> [1..1] CodeSet 2282
             LockReason <LckRsn> [0..*] Text 2283
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities 2258 August 2026
```

