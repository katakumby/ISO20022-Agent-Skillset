---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["42 reda.022.001.02 PartyModificationRequestV02", "42.2 Structure"]
file_pages: [2141]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.022.001.02"]
---

# 42.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2141 to 2141.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2141

```text
42.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PtyModReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2142
   SystemPartyIdentification <SysPtyId> [1..1] ± 2142
   Modification <Mod> [1..*]  2143
     ScopeIndication <ScpIndctn> [1..1] CodeSet 2145
     RequestedModification <ReqdMod> [1..1]  2145
{Or       SystemPartyDate <SysPtyDt> [1..1]  2146
         OpeningDate <OpngDt> [0..1] Date 2147
         ClosingDate <ClsgDt> [0..1] Date 2147
Or       PartyIdentification <PtyId> [1..1]  2147
         ValidFrom <VldFr> [0..1] Date 2147
         Identification <Id> [0..1] ± 2147
Or       PartyName <PtyNm> [1..1]  2148
         ValidFrom <VldFr> [0..1] Date 2148
         Name <Nm> [0..1] Text 2148
         ShortName <ShrtNm> [0..1] Text 2148
Or       ContactDetails <CtctDtls> [1..1] ± 2148
Or       TechnicalAddress <TechAdr> [1..1]  2149
{Or         BICFI <BICFI> [1..1] IdentifierSet C2 2149
Or}         TechnicalAddress <TechAdr> [1..1] Text 2150
Or       PartyAddress <PtyAdr> [1..1] ± 2150
Or       ResidenceType <ResTp> [1..1] CodeSet 2151
Or       LockStatus <LckSts> [1..1]  2152
         ValidFrom <VldFr> [0..1] Date 2152
         Status <Sts> [1..1] CodeSet 2152
         LockReason <LckRsn> [0..*] Text 2152
Or       SystemRestriction <SysRstrctn> [1..1]  2152
         ValidFrom <VldFr> [1..1] DateTime 2153
         ValidTo <VldTo> [0..1] DateTime 2153
         Type <Tp> [1..1] Text 2153
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.022.001.02 PartyModificationRequestV02
Target2-Securities 2141 August 2026
```

