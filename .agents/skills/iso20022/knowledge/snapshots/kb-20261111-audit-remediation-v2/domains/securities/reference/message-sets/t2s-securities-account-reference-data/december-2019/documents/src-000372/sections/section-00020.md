---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["3 reda.019.001.01 SecuritiesAccountQueryV01", "3.4 Message Building Blocks", "3.4.2 SearchCriteria <SchCrit>", "3.4.2.7 AccountType <AcctTp>"]
file_pages: [22]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.019.001.01"]
---

# 3.4.2.7 AccountType <AcctTp>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 22 to 22.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 22

```text
3.4.2.7  AccountType <AcctTp>
Presence: [0..1]
Definition: Specifies the type of securities account.
AccountType <AcctTp> contains one of the following SystemSecuritiesAccountType1Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 22
Or}   Proprietary <Prtry> [1..1] ± 22
3.4.2.7.1  Code <Cd>
Presence: [1..1]
Definition: System securities account type, in a coded form.
Datatype: "SystemSecuritiesAccountType1Code" on page 96
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
3.4.2.7.2  Proprietary <Prtry>
Presence: [1..1]
Definition: System securities account type, in a proprietary form.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 81 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 81
   Issuer <Issr> [1..1] Text 81
   SchemeName <SchmeNm> [0..1] Text 81
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.019.001.01 SecuritiesAccountQueryV01
Target2-Securities - Securities Account Reference Data 22 December 2019
```

