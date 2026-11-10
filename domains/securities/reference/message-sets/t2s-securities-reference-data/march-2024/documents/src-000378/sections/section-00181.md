---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.2 CommonFinancialInstrumentAttributes12", "13.1.6.2.12 LegalRestrictions <LglRstrctns>"]
file_pages: [258]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.2.12 LegalRestrictions <LglRstrctns>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 258 to 258.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 258

```text
13.1.6.2.12  LegalRestrictions <LglRstrctns>
Presence: [0..1]
Definition: Specifies the regulatory restrictions applicable to a security.
LegalRestrictions <LglRstrctns> contains one of the following LegalRestrictions4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 258
Or}   Proprietary <Prtry> [1..1] ± 258
13.1.6.2.12.1  Code <Cd>
Presence: [1..1]
Definition: Legal restrictions expressed as an ISO 20022 code.
Datatype: "LegalRestrictions1Code" on page 518
CodeName Name Definition
USLE USLegal144A Ownership or transfer of an unregistered
security issued, pursuant to US legal
restrictions 144A.
NORE NoRestrictions Ownership or transfer of a security that
is not subject to restrictions.
REST Restrictions Ownership or transfer of a security that
is subject to restrictions, and not
pursuant to 144A.
13.1.6.2.12.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Legal restrictions expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.6.2.13  PositionLimit <PosLmt>
Presence: [0..1]
Definition: Position limits are created for the purpose of maintaining stable and fair markets. Contracts
held by one individual investor with different brokers may be combined in order to gauge accurately the
level of control held by one party.
Each option and futures contract will have varying position limits.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 258 March 2024
```

