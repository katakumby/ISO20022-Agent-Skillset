---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.9 FundParties <FndPties>"]
file_pages: [321]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.9 FundParties <FndPties>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 321 to 321.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 321

```text
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
15.4.5.9  FundParties <FndPties>
Presence: [0..1]
Definition: Parties related to the investment fund.
FundParties <FndPties> contains the following elements (see "FundParties1" on page 5001 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Guarantor <Guarntr> [0..1] ± 5001
   Auditor <Audtr> [0..1] ± 5002
   Trustee <Trstee> [0..1] ± 5002
   OtherParty <OthrPty> [0..*] ± 5003
15.4.5.10  MainFundOrderDesk <MainFndOrdrDsk>
Presence: [0..1]
Definition: Principal entity appointed by the fund, to which orders should be submitted. Usually located
in the country of domicile.
MainFundOrderDesk <MainFndOrdrDsk> contains the following elements (see "OrderDesk1" on
page 4959 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OrderDesk <OrdrDsk> [0..1] ± 4959
   ClosureDates <ClsrDts> [0..*] Date 4959
   AdditionalInformation <AddtlInf> [0..*] ± 4959
15.4.5.11  FundManagementCompany <FndMgmtCpny>
Presence: [0..1]
Definition: Company that is responsible for the management and operation of the fund, for example,
determines the investment strategy, appoints the service providers, and makes major decisions for the
fund. It is usually responsible for the distribution and marketing of the fund. For self-managed funds, this
will often be a separate promoter or sponsor of the fund.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 321 May 2026
```

