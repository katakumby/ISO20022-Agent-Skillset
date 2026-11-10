---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["5 reda.021.001.01 SecuritiesAccountReportV01", "5.4 Message Building Blocks", "5.4.3 ReportOrError <RptOrErr>", "5.4.3.1 SecuritiesAccountReport <SctiesAcctRpt>", "5.4.3.1.2 SecuritiesAccountOrError <SctiesAcctOrErr>", "5.4.3.1.2.1 SecuritiesAccount <SctiesAcct>", "5.4.3.1.2.1.5 Type <Tp>", "5.4.3.1.2.1.5.2 Proprietary <Prtry>"]
file_pages: [43]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.021.001.01"]
---

# 5.4.3.1.2.1.5.2 Proprietary <Prtry>

Source: [src-000372](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 43 to 43.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 43

```text
CodeName Name Definition
CSDO CSDOmnibusAccount Account operated by CSD in cross-CSD
settlement context.
ISSA IssuanceAccount Account reflecting the holdings of the
participants of the issuer CSD for a given
financial instrument.
5.4.3.1.2.1.5.2  Proprietary <Prtry>
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
5.4.3.1.2.1.6  AccountOwner <AcctOwnr>
Presence: [1..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "SystemPartyIdentification8" on
page 91 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 91
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 91
5.4.3.1.2.1.7  PartyType <PtyTp>
Presence: [0..1]
Definition: Specifies the type of party owning the account.
PartyType <PtyTp> contains one of the following SystemPartyType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 43
Or}   Proprietary <Prtry> [1..1] Text 44
5.4.3.1.2.1.7.1  Code <Cd>
Presence: [1..1]
Definition: System party type, in a coded format.
Datatype: "ExternalSystemPartyType1Code" on page 95
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.021.001.01 SecuritiesAccountReportV01
Target2-Securities - Securities Account Reference Data 43 December 2019
```

