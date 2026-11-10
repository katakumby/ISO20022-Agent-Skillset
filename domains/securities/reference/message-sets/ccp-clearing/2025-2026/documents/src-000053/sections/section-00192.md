---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["7 MX secl.006.001.02 DefaultFundContributionReportV02", "7.4 Message Building Blocks", "7.4.1 ReportParameters <RptParams>", "7.4.1.5 CalculationDate <ClctnDt>"]
file_pages: [251]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.006.001.02"]
---

# 7.4.1.5 CalculationDate <ClctnDt>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 251 to 251.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 251

```text
Constraints
• ValidationByTable
(Rule)
Must be a valid currency code which is registered with the ISO 4217 Maintenance Agency, and
consist of three contiguous letters.
7.4.1.5  CalculationDate <ClctnDt>
Presence: [0..1]
Definition: Indicates the date of calculation of the deficit (if any).
Datatype: ISODateTime on page 487
7.4.2 ClearingMember <ClrMmb>
Presence: [1..1]
Definition: Provides the identification of the account owner, that is the clearing member (individual
clearing member or general clearing member).
ClearingMember <ClrMmb> contains one of the following elements (see PartyIdentification35Choice
on page 452 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C4 452
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 452
7.4.3 ReportDetails <RptDtls>
Presence: [1..*]
Definition: Provides details on the default fund report.
ReportDetails <RptDtls> contains the following DefaultFundReport1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DefaultFundCalculation <DfltFndClctn> [1..*] ± 251
   CollateralDescription <CollDesc> [1..*] ± 252
   NetExcessOrDeficit <NetXcssOrDfcit> [1..1] ± 252
7.4.3.1  DefaultFundCalculation <DfltFndClctn>
Presence: [1..*]
Definition: Provides details about the calculation of the clearing member contribution to the default fund.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.006.001.02
DefaultFundContributionReportV02
March 2026 251
```

