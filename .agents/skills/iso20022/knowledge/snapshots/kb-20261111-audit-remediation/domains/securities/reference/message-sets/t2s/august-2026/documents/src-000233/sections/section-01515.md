---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["41 reda.021.001.01 SecuritiesAccountReportV01", "41.4 Message Building Blocks", "41.4.3 ReportOrError <RptOrErr>", "41.4.3.1 SecuritiesAccountReport <SctiesAcctRpt>", "41.4.3.1.2 SecuritiesAccountOrError <SctiesAcctOrErr>", "41.4.3.1.2.1 SecuritiesAccount <SctiesAcct>", "41.4.3.1.2.1.5 Type <Tp>", "41.4.3.1.2.1.5.2 Proprietary <Prtry>"]
file_pages: [2135]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.021.001.01"]
---

# 41.4.3.1.2.1.5.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2135 to 2135.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2135

```text
CodeName Name Definition
CSDO CSDOmnibusAccount Account operated by CSD in cross-CSD
settlement context.
ISSA IssuanceAccount Account reflecting the holdings of the
participants of the issuer CSD for a given
financial instrument.
41.4.3.1.2.1.5.2  Proprietary <Prtry>
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
41.4.3.1.2.1.6  AccountOwner <AcctOwnr>
Presence: [1..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "SystemPartyIdentification8" on
page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
41.4.3.1.2.1.7  PartyType <PtyTp>
Presence: [0..1]
Definition: Specifies the type of party owning the account.
PartyType <PtyTp> contains one of the following SystemPartyType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2135
Or}   Proprietary <Prtry> [1..1] Text 2136
41.4.3.1.2.1.7.1  Code <Cd>
Presence: [1..1]
Definition: System party type, in a coded format.
Datatype: "ExternalSystemPartyType1Code" on page 3246
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.021.001.01 SecuritiesAccountReportV01
Target2-Securities 2135 August 2026
```

