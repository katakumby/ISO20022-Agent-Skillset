---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["39 reda.019.001.01 SecuritiesAccountQueryV01", "39.4 Message Building Blocks", "39.4.2 SearchCriteria <SchCrit>", "39.4.2.7 AccountType <AcctTp>"]
file_pages: [2114]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.019.001.01"]
---

# 39.4.2.7 AccountType <AcctTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2114 to 2114.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2114

```text
39.4.2.7  AccountType <AcctTp>
Presence: [0..1]
Definition: Specifies the type of securities account.
AccountType <AcctTp> contains one of the following SystemSecuritiesAccountType1Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2114
Or}   Proprietary <Prtry> [1..1] ± 2114
39.4.2.7.1  Code <Cd>
Presence: [1..1]
Definition: System securities account type, in a coded form.
Datatype: "SystemSecuritiesAccountType1Code" on page 3305
CodeName Name Definition
CSDP CSDParticipantAccount Account owned by a CSD Participant
.
CSDM CSDMirrorAccount Account operated by CSD for mirroring
positions
.
ICSA InterCSDAccount Account operated by CSD for settlement
of securities legs for instructions
involving internal CSD s.
TOFF TechnicalOffsetAccount Account operated by CSDs in a direct
holding market context.
CSDO CSDOmnibusAccount Account operated by CSD in cross-CSD
settlement context.
ISSA IssuanceAccount Account reflecting the holdings of the
participants of the issuer CSD for a given
financial instrument.
39.4.2.7.2  Proprietary <Prtry>
Presence: [1..1]
Definition: System securities account type, in a proprietary form.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.019.001.01 SecuritiesAccountQueryV01
Target2-Securities 2114 August 2026
```

