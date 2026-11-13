---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["2 reda.018.001.01 SecuritiesAccountCreationRequestV01", "2.4 Message Building Blocks", "2.4.2 SecuritiesAccount <SctiesAcct>", "2.4.2.3 Type <Tp>"]
file_pages: [10]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.018.001.01"]
---

# 2.4.2.3 Type <Tp>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 10 to 10.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 10

```text
Datatype: "Max35Text" on page 100
2.4.2.3  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of the securities account.
Type <Tp> contains one of the following SystemSecuritiesAccountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 10
Or}   Proprietary <Prtry> [1..1] ± 10
2.4.2.3.1  Code <Cd>
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
2.4.2.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: System securities account type, in a proprietary form.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.018.001.01
SecuritiesAccountCreationRequestV01
Target2-Securities - Securities Account Reference Data 10 December 2019
```

