---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.17 NettingEligibility4Choice", "35.1.16.17.2 Proprietary <Prtry>"]
file_pages: [1549]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.17.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1549 to 1549.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1549

```text
• Meaning When True: Yes
• Meaning When False: No
35.1.16.17.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Netting eligibility expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.18  Role6Choice
Definition: Choice of format for a party role.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1549
Or   Proprietary <Prtry> [1..1] ± 1550
Or}   Text <Txt> [1..1] Text 1550
35.1.16.18.1  Code <Cd>
Presence: [1..1]
Definition: Role of the party in the activity expressed as an ISO 20022 code.
Datatype: "InvestmentFundRole2Code" on page 2084
CodeName Name Definition
FMCO FundManagementCompany Party that sets up a fund, decides upon
the investment strategy, appoints
agents, and is responsible for the
promotion and the marketing of the fund.
This party makes all the strategic
decisions related to a fund.
REGI Registrar Party responsible for keeping track of the
owners of securities. In the investment
fund business, this party keeps the
investor registry of the fund, and
administers investor accounts and
related records. It is appointed by the
fund management company.
TRAG TransferAgent Party appointed by the fund
management company. This party
updates records of investor accounts to
reflect the daily investor purchases,
redemptions, switches, transfers, and re-
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1549 March 2026
```

