---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["6 reda.022.001.02 PartyModificationRequestV02", "6.4 Message Building Blocks", "6.4.3 Modification <Mod>"]
file_pages: [64, 65]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.022.001.02"]
---

# 6.4.3 Modification <Mod>

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 64 to 65.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 64

```text
Definition: Unique identification, as assigned by the executing system, to unambiguously identify the
party to be modified.
SystemPartyIdentification <SysPtyId> contains the following elements (see
"SystemPartyIdentification8" on page 170 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 170
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 170
6.4.3 Modification <Mod>
Presence: [1..*]
Definition: Identifies the list of requested modifications to be executed by the system.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.022.001.02 PartyModificationRequestV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
64 March 2024
```

## File page 65

```text
Modification <Mod> contains the following SystemPartyModification3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ScopeIndication <ScpIndctn> [1..1] CodeSet 66
   RequestedModification <ReqdMod> [1..1]  66
{Or     SystemPartyDate <SysPtyDt> [1..1]  67
       OpeningDate <OpngDt> [0..1] Date 68
       ClosingDate <ClsgDt> [0..1] Date 68
Or     PartyIdentification <PtyId> [1..1]  68
       ValidFrom <VldFr> [0..1] Date 68
       Identification <Id> [0..1] ± 68
Or     PartyName <PtyNm> [1..1]  69
       ValidFrom <VldFr> [0..1] Date 69
       Name <Nm> [0..1] Text 69
       ShortName <ShrtNm> [0..1] Text 69
Or     ContactDetails <CtctDtls> [1..1] ± 69
Or     TechnicalAddress <TechAdr> [1..1]  70
{Or       BICFI <BICFI> [1..1] IdentifierSet C2 70
Or}       TechnicalAddress <TechAdr> [1..1] Text 71
Or     PartyAddress <PtyAdr> [1..1] ± 71
Or     ResidenceType <ResTp> [1..1] CodeSet 72
Or     LockStatus <LckSts> [1..1]  73
       ValidFrom <VldFr> [0..1] Date 73
       Status <Sts> [1..1] CodeSet 73
       LockReason <LckRsn> [0..*] Text 73
Or     SystemRestriction <SysRstrctn> [1..1]  73
       ValidFrom <VldFr> [1..1] DateTime 74
       ValidTo <VldTo> [0..1] DateTime 74
       Type <Tp> [1..1] Text 74
Or}     MarketSpecificAttribute <MktSpcfcAttr> [1..1]  74
       Name <Nm> [1..1] Text 74
       Value <Val> [1..1] Text 74
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.022.001.02 PartyModificationRequestV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
65 March 2024
```

