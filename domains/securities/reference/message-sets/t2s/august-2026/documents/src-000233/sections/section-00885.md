---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.2 Delete <Del>", "28.4.2.1.2.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.2.2.12 LegalRestrictions <LglRstrctns>"]
file_pages: [1310]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.2.2.12 LegalRestrictions <LglRstrctns>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1310 to 1310.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1310

```text
28.4.2.1.2.2.12  LegalRestrictions <LglRstrctns>
Presence: [0..1]
Definition: Specifies the regulatory restrictions applicable to a security.
LegalRestrictions <LglRstrctns> contains one of the following LegalRestrictions4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1310
Or}   Proprietary <Prtry> [1..1] ± 1310
28.4.2.1.2.2.12.1  Code <Cd>
Presence: [1..1]
Definition: Legal restrictions expressed as an ISO 20022 code.
Datatype: "LegalRestrictions1Code" on page 3261
CodeName Name Definition
USLE USLegal144A Ownership or transfer of an unregistered
security issued, pursuant to US legal
restrictions 144A.
NORE NoRestrictions Ownership or transfer of a security that
is not subject to restrictions.
REST Restrictions Ownership or transfer of a security that
is subject to restrictions, and not
pursuant to 144A.
28.4.2.1.2.2.12.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Legal restrictions expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
28.4.2.1.2.2.13  PositionLimit <PosLmt>
Presence: [0..1]
Definition: Position limits are created for the purpose of maintaining stable and fair markets. Contracts
held by one individual investor with different brokers may be combined in order to gauge accurately the
level of control held by one party.
Each option and futures contract will have varying position limits.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1310 August 2026
```

