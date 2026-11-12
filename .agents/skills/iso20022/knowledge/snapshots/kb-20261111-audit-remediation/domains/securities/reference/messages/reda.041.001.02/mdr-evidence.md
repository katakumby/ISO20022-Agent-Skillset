---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.041.001.02"
message_family: "reda.041"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02"
source_ids: ["src-000233", "src-000369"]
source_locations: [{"source_id": "src-000233", "heading": "58 reda.041.001.02 PartyActivityAdviceV02", "file_pages": [2256, 2287]}, {"source_id": "src-000369", "heading": "8 reda.041.001.02 PartyActivityAdviceV02", "file_pages": [79, 110]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# reda.041.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 58 reda.041.001.02 PartyActivityAdviceV02

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp2256–2287; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 58 reda.041.001.02 PartyActivityAdviceV02, Functionality, file p2256.**

The PartyActivityReport message is sent by the executing party to an instructing party containing
information about changes on party reference data.
Scope and usage:
It aims at informing about the changes occurred during a business date for party reference data.
Outline
The PartyActivityAdviceV02 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. PartyActivity
Activity report of changes occurred for a party defined in the system.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities 2256 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [58 reda.041.001.02 PartyActivityAdviceV02](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01629.md) | 2256–2256 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01630.md) | 2257–2258 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01631.md); [Constraints continuation C4 (file p2260)](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01632.md#file-page-2260) | 2259–2259 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01632.md) | 2260–2262 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.4 Message Building Blocks / 58.4.2 PartyActivity &lt;PtyActvty&gt; / 58.4.2.1 SystemDate &lt;SysDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01633.md) | 2263–2265 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.4 Message Building Blocks / 58.4.2 PartyActivity &lt;PtyActvty&gt; / 58.4.2.2 Change &lt;Chng&gt; / 58.4.2.2.1 PartyIdentification &lt;PtyId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01634.md) | 2266–2268 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.4 Message Building Blocks / 58.4.2 PartyActivity &lt;PtyActvty&gt; / 58.4.2.2 Change &lt;Chng&gt; / 58.4.2.2.2 Record &lt;Rcrd&gt; / 58.4.2.2.2.1 Address &lt;Adr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01635.md) | 2269–2269 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.4 Message Building Blocks / 58.4.2 PartyActivity &lt;PtyActvty&gt; / 58.4.2.2 Change &lt;Chng&gt; / 58.4.2.2.2 Record &lt;Rcrd&gt; / 58.4.2.2.2.1 Address &lt;Adr&gt; / 58.4.2.2.2.1.2 New &lt;New&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01636.md) | 2270–2270 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.4 Message Building Blocks / 58.4.2 PartyActivity &lt;PtyActvty&gt; / 58.4.2.2 Change &lt;Chng&gt; / 58.4.2.2.2 Record &lt;Rcrd&gt; / 58.4.2.2.2.2 ContactDetails &lt;CtctDtls&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01637.md) | 2271–2271 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.4 Message Building Blocks / 58.4.2 PartyActivity &lt;PtyActvty&gt; / 58.4.2.2 Change &lt;Chng&gt; / 58.4.2.2.2 Record &lt;Rcrd&gt; / 58.4.2.2.2.2 ContactDetails &lt;CtctDtls&gt; / 58.4.2.2.2.2.2 New &lt;New&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01638.md) | 2272–2272 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.4 Message Building Blocks / 58.4.2 PartyActivity &lt;PtyActvty&gt; / 58.4.2.2 Change &lt;Chng&gt; / 58.4.2.2.2 Record &lt;Rcrd&gt; / 58.4.2.2.2.3 OpeningDate &lt;OpngDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01639.md) | 2273–2273 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.4 Message Building Blocks / 58.4.2 PartyActivity &lt;PtyActvty&gt; / 58.4.2.2 Change &lt;Chng&gt; / 58.4.2.2.2 Record &lt;Rcrd&gt; / 58.4.2.2.2.4 ClosingDate &lt;ClsgDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01640.md) | 2274–2274 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.4 Message Building Blocks / 58.4.2 PartyActivity &lt;PtyActvty&gt; / 58.4.2.2 Change &lt;Chng&gt; / 58.4.2.2.2 Record &lt;Rcrd&gt; / 58.4.2.2.2.5 Type &lt;Tp&gt; / 58.4.2.2.2.5.1 Old &lt;Od&gt; / 58.4.2.2.2.5.1.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01641.md) | 2275–2275 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.4 Message Building Blocks / 58.4.2 PartyActivity &lt;PtyActvty&gt; / 58.4.2.2 Change &lt;Chng&gt; / 58.4.2.2.2 Record &lt;Rcrd&gt; / 58.4.2.2.2.6 TechnicalAddress &lt;TechAdr&gt; / 58.4.2.2.2.6.1 Old &lt;Od&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01642.md) | 2276–2276 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.4 Message Building Blocks / 58.4.2 PartyActivity &lt;PtyActvty&gt; / 58.4.2.2 Change &lt;Chng&gt; / 58.4.2.2.2 Record &lt;Rcrd&gt; / 58.4.2.2.2.6 TechnicalAddress &lt;TechAdr&gt; / 58.4.2.2.2.6.2 New &lt;New&gt; / 58.4.2.2.2.6.2.1 BICFI &lt;BICFI&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01643.md) | 2277–2277 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.4 Message Building Blocks / 58.4.2 PartyActivity &lt;PtyActvty&gt; / 58.4.2.2 Change &lt;Chng&gt; / 58.4.2.2.2 Record &lt;Rcrd&gt; / 58.4.2.2.2.7 MarketSpecificAttribute &lt;MktSpcfcAttr&gt; / 58.4.2.2.2.7.1 Old &lt;Od&gt; / 58.4.2.2.2.7.1.1 Name &lt;Nm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01644.md) | 2278–2278 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.4 Message Building Blocks / 58.4.2 PartyActivity &lt;PtyActvty&gt; / 58.4.2.2 Change &lt;Chng&gt; / 58.4.2.2.2 Record &lt;Rcrd&gt; / 58.4.2.2.2.8 Name &lt;Nm&gt; / 58.4.2.2.2.8.1 Old &lt;Od&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01645.md) | 2279–2279 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.4 Message Building Blocks / 58.4.2 PartyActivity &lt;PtyActvty&gt; / 58.4.2.2 Change &lt;Chng&gt; / 58.4.2.2.2 Record &lt;Rcrd&gt; / 58.4.2.2.2.8 Name &lt;Nm&gt; / 58.4.2.2.2.8.2 New &lt;New&gt; / 58.4.2.2.2.8.2.1 ValidFrom &lt;VldFr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01646.md) | 2280–2280 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.4 Message Building Blocks / 58.4.2 PartyActivity &lt;PtyActvty&gt; / 58.4.2.2 Change &lt;Chng&gt; / 58.4.2.2.2 Record &lt;Rcrd&gt; / 58.4.2.2.2.9 ResidenceType &lt;ResTp&gt; / 58.4.2.2.2.9.2 New &lt;New&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01647.md) | 2281–2281 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.4 Message Building Blocks / 58.4.2 PartyActivity &lt;PtyActvty&gt; / 58.4.2.2 Change &lt;Chng&gt; / 58.4.2.2.2 Record &lt;Rcrd&gt; / 58.4.2.2.2.10 LockStatus &lt;LckSts&gt; / 58.4.2.2.2.10.1 Old &lt;Od&gt; / 58.4.2.2.2.10.1.1 ValidFrom &lt;VldFr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01648.md) | 2282–2282 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.4 Message Building Blocks / 58.4.2 PartyActivity &lt;PtyActvty&gt; / 58.4.2.2 Change &lt;Chng&gt; / 58.4.2.2.2 Record &lt;Rcrd&gt; / 58.4.2.2.2.10 LockStatus &lt;LckSts&gt; / 58.4.2.2.2.10.2 New &lt;New&gt; / 58.4.2.2.2.10.2.3 LockReason &lt;LckRsn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01649.md) | 2283–2283 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.4 Message Building Blocks / 58.4.2 PartyActivity &lt;PtyActvty&gt; / 58.4.2.2 Change &lt;Chng&gt; / 58.4.2.2.2 Record &lt;Rcrd&gt; / 58.4.2.2.2.11 Restriction &lt;Rstrctn&gt; / 58.4.2.2.2.11.1 Old &lt;Od&gt; / 58.4.2.2.2.11.1.1 RestrictionType &lt;RstrctnTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01650.md) | 2284–2284 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.4 Message Building Blocks / 58.4.2 PartyActivity &lt;PtyActvty&gt; / 58.4.2.2 Change &lt;Chng&gt; / 58.4.2.2.2 Record &lt;Rcrd&gt; / 58.4.2.2.2.11 Restriction &lt;Rstrctn&gt; / 58.4.2.2.2.11.2 New &lt;New&gt; / 58.4.2.2.2.11.2.1 RestrictionType &lt;RstrctnTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01651.md) | 2285–2285 |
| [58 reda.041.001.02 PartyActivityAdviceV02 / 58.4 Message Building Blocks / 58.4.2 PartyActivity &lt;PtyActvty&gt; / 58.4.2.2 Change &lt;Chng&gt; / 58.4.2.2.2 Record &lt;Rcrd&gt; / 58.4.2.2.2.11 Restriction &lt;Rstrctn&gt; / 58.4.2.2.2.11.2 New &lt;New&gt; / 58.4.2.2.2.11.2.3 ValidUntil &lt;VldUntil&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01652.md) | 2286–2287 |

## src-000369 — 8 reda.041.001.02 PartyActivityAdviceV02

[src-000369](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`; file pp79–110; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000369, 8 reda.041.001.02 PartyActivityAdviceV02, Functionality, file p79.**

The PartyActivityReport message is sent by the executing party to an instructing party containing
information about changes on party reference data.
Scope and usage:
It aims at informing about the changes occurred during a business date for party reference data.
Outline
The PartyActivityAdviceV02 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. PartyActivity
Activity report of changes occurred for a party defined in the system.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
79 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [8 reda.041.001.02 PartyActivityAdviceV02](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00066.md) | 79–79 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.2 Structure](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00067.md) | 80–81 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.3 Constraints](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00068.md); [Constraints continuation C4 (file p83)](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00069.md#file-page-83) | 82–82 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.4 Message Building Blocks](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00069.md) | 83–85 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.4 Message Building Blocks / 8.4.2 PartyActivity &lt;PtyActvty&gt; / 8.4.2.1 SystemDate &lt;SysDt&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00070.md) | 86–88 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.4 Message Building Blocks / 8.4.2 PartyActivity &lt;PtyActvty&gt; / 8.4.2.2 Change &lt;Chng&gt; / 8.4.2.2.1 PartyIdentification &lt;PtyId&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00071.md) | 89–91 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.4 Message Building Blocks / 8.4.2 PartyActivity &lt;PtyActvty&gt; / 8.4.2.2 Change &lt;Chng&gt; / 8.4.2.2.2 Record &lt;Rcrd&gt; / 8.4.2.2.2.1 Address &lt;Adr&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00072.md) | 92–92 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.4 Message Building Blocks / 8.4.2 PartyActivity &lt;PtyActvty&gt; / 8.4.2.2 Change &lt;Chng&gt; / 8.4.2.2.2 Record &lt;Rcrd&gt; / 8.4.2.2.2.1 Address &lt;Adr&gt; / 8.4.2.2.2.1.2 New &lt;New&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00073.md) | 93–93 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.4 Message Building Blocks / 8.4.2 PartyActivity &lt;PtyActvty&gt; / 8.4.2.2 Change &lt;Chng&gt; / 8.4.2.2.2 Record &lt;Rcrd&gt; / 8.4.2.2.2.2 ContactDetails &lt;CtctDtls&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00074.md) | 94–94 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.4 Message Building Blocks / 8.4.2 PartyActivity &lt;PtyActvty&gt; / 8.4.2.2 Change &lt;Chng&gt; / 8.4.2.2.2 Record &lt;Rcrd&gt; / 8.4.2.2.2.2 ContactDetails &lt;CtctDtls&gt; / 8.4.2.2.2.2.2 New &lt;New&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00075.md) | 95–95 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.4 Message Building Blocks / 8.4.2 PartyActivity &lt;PtyActvty&gt; / 8.4.2.2 Change &lt;Chng&gt; / 8.4.2.2.2 Record &lt;Rcrd&gt; / 8.4.2.2.2.3 OpeningDate &lt;OpngDt&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00076.md) | 96–96 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.4 Message Building Blocks / 8.4.2 PartyActivity &lt;PtyActvty&gt; / 8.4.2.2 Change &lt;Chng&gt; / 8.4.2.2.2 Record &lt;Rcrd&gt; / 8.4.2.2.2.4 ClosingDate &lt;ClsgDt&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00077.md) | 97–97 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.4 Message Building Blocks / 8.4.2 PartyActivity &lt;PtyActvty&gt; / 8.4.2.2 Change &lt;Chng&gt; / 8.4.2.2.2 Record &lt;Rcrd&gt; / 8.4.2.2.2.5 Type &lt;Tp&gt; / 8.4.2.2.2.5.1 Old &lt;Od&gt; / 8.4.2.2.2.5.1.1 Code &lt;Cd&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00078.md) | 98–98 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.4 Message Building Blocks / 8.4.2 PartyActivity &lt;PtyActvty&gt; / 8.4.2.2 Change &lt;Chng&gt; / 8.4.2.2.2 Record &lt;Rcrd&gt; / 8.4.2.2.2.6 TechnicalAddress &lt;TechAdr&gt; / 8.4.2.2.2.6.1 Old &lt;Od&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00079.md) | 99–99 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.4 Message Building Blocks / 8.4.2 PartyActivity &lt;PtyActvty&gt; / 8.4.2.2 Change &lt;Chng&gt; / 8.4.2.2.2 Record &lt;Rcrd&gt; / 8.4.2.2.2.6 TechnicalAddress &lt;TechAdr&gt; / 8.4.2.2.2.6.2 New &lt;New&gt; / 8.4.2.2.2.6.2.1 BICFI &lt;BICFI&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00080.md) | 100–100 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.4 Message Building Blocks / 8.4.2 PartyActivity &lt;PtyActvty&gt; / 8.4.2.2 Change &lt;Chng&gt; / 8.4.2.2.2 Record &lt;Rcrd&gt; / 8.4.2.2.2.7 MarketSpecificAttribute &lt;MktSpcfcAttr&gt; / 8.4.2.2.2.7.1 Old &lt;Od&gt; / 8.4.2.2.2.7.1.1 Name &lt;Nm&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00081.md) | 101–101 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.4 Message Building Blocks / 8.4.2 PartyActivity &lt;PtyActvty&gt; / 8.4.2.2 Change &lt;Chng&gt; / 8.4.2.2.2 Record &lt;Rcrd&gt; / 8.4.2.2.2.8 Name &lt;Nm&gt; / 8.4.2.2.2.8.1 Old &lt;Od&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00082.md) | 102–102 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.4 Message Building Blocks / 8.4.2 PartyActivity &lt;PtyActvty&gt; / 8.4.2.2 Change &lt;Chng&gt; / 8.4.2.2.2 Record &lt;Rcrd&gt; / 8.4.2.2.2.8 Name &lt;Nm&gt; / 8.4.2.2.2.8.2 New &lt;New&gt; / 8.4.2.2.2.8.2.1 ValidFrom &lt;VldFr&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00083.md) | 103–103 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.4 Message Building Blocks / 8.4.2 PartyActivity &lt;PtyActvty&gt; / 8.4.2.2 Change &lt;Chng&gt; / 8.4.2.2.2 Record &lt;Rcrd&gt; / 8.4.2.2.2.9 ResidenceType &lt;ResTp&gt; / 8.4.2.2.2.9.2 New &lt;New&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00084.md) | 104–104 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.4 Message Building Blocks / 8.4.2 PartyActivity &lt;PtyActvty&gt; / 8.4.2.2 Change &lt;Chng&gt; / 8.4.2.2.2 Record &lt;Rcrd&gt; / 8.4.2.2.2.10 LockStatus &lt;LckSts&gt; / 8.4.2.2.2.10.1 Old &lt;Od&gt; / 8.4.2.2.2.10.1.1 ValidFrom &lt;VldFr&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00085.md) | 105–105 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.4 Message Building Blocks / 8.4.2 PartyActivity &lt;PtyActvty&gt; / 8.4.2.2 Change &lt;Chng&gt; / 8.4.2.2.2 Record &lt;Rcrd&gt; / 8.4.2.2.2.10 LockStatus &lt;LckSts&gt; / 8.4.2.2.2.10.2 New &lt;New&gt; / 8.4.2.2.2.10.2.3 LockReason &lt;LckRsn&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00086.md) | 106–106 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.4 Message Building Blocks / 8.4.2 PartyActivity &lt;PtyActvty&gt; / 8.4.2.2 Change &lt;Chng&gt; / 8.4.2.2.2 Record &lt;Rcrd&gt; / 8.4.2.2.2.11 Restriction &lt;Rstrctn&gt; / 8.4.2.2.2.11.1 Old &lt;Od&gt; / 8.4.2.2.2.11.1.1 RestrictionType &lt;RstrctnTp&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00087.md) | 107–107 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.4 Message Building Blocks / 8.4.2 PartyActivity &lt;PtyActvty&gt; / 8.4.2.2 Change &lt;Chng&gt; / 8.4.2.2.2 Record &lt;Rcrd&gt; / 8.4.2.2.2.11 Restriction &lt;Rstrctn&gt; / 8.4.2.2.2.11.2 New &lt;New&gt; / 8.4.2.2.2.11.2.1 RestrictionType &lt;RstrctnTp&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00088.md) | 108–108 |
| [8 reda.041.001.02 PartyActivityAdviceV02 / 8.4 Message Building Blocks / 8.4.2 PartyActivity &lt;PtyActvty&gt; / 8.4.2.2 Change &lt;Chng&gt; / 8.4.2.2.2 Record &lt;Rcrd&gt; / 8.4.2.2.2.11 Restriction &lt;Rstrctn&gt; / 8.4.2.2.2.11.2 New &lt;New&gt; / 8.4.2.2.2.11.2.3 ValidUntil &lt;VldUntil&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00089.md) | 109–110 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Bank](../../../../../shared/reference/participants/participant-src-000368-bank.md) | participant | src-000368 |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000368-central-securities-depositories-csd.md) | participant | src-000368 |
| [Corporate](../../../../../shared/reference/participants/participant-src-000368-corporate.md) | participant | src-000368 |
| [CSD](../../../../../shared/reference/participants/participant-src-000368-csd.md) | participant | src-000368 |
| [Executing / Servicing Party](../../../../../shared/reference/participants/participant-src-000368-executing-servicing-party.md) | participant | src-000368 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000368-instructing-party.md) | participant | src-000368 |
| [Market Data Provider](../../../../../shared/reference/participants/participant-src-000368-market-data-provider.md) | participant | src-000368 |
| [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000368-market-infrastructure.md) | participant | src-000368 |
| [National Central Bank (NCB)](../../../../../shared/reference/participants/participant-src-000368-national-central-bank-ncb.md) | participant | src-000368 |
| [Create Party](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p120-create-party.md) | business-flow | src-000368 |
| [Modify Party](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p122-modify-party.md) | business-flow | src-000368 |
| [Delete Party](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p124-delete-party.md) | business-flow | src-000368 |
| [Query](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p126-query.md) | business-flow | src-000368 |
| [Statement](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p128-statement.md) | business-flow | src-000368 |
| [Creation Process](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p133-creation-process.md) | business-flow | src-000368 |
| [Modification Process](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p137-modification-process.md) | business-flow | src-000368 |
| [Deletion Process](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p140-deletion-process.md) | business-flow | src-000368 |
| [Query/Query Response process](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p144-query-query-response-process.md) | business-flow | src-000368 |
| [Statement process](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p147-statement-process.md) | business-flow | src-000368 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)



<!-- PARTY-FLOWS -->
## Party reference data flows

- [Receive an unsolicited party activity statement](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p128-statement.md)
