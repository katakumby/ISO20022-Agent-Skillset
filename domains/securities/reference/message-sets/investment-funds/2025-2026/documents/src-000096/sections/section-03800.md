---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.7 IndividualPerson38", "66.1.32.7.14 EmployingCompany <EmplngCpny>"]
file_pages: [5089]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.7.14 EmployingCompany <EmplngCpny>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5089 to 5089.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5089

```text
• Meaning When True: Yes
• Meaning When False: No
66.1.32.7.14  EmployingCompany <EmplngCpny>
Presence: [0..1]
Definition: Organisation represented by a person, or for which a person works.
Datatype: "Max140Text" on page 5402
66.1.32.7.15  BusinessFunction <BizFctn>
Presence: [0..1]
Definition: Title of the function.
Datatype: "Max35Text" on page 5403
66.1.32.7.16  PoliticallyExposedPerson <PltclyXpsdPrsn>
Presence: [0..1]
Definition: Politically exposed person checks.
Impacted by: C29 "PoliticallyExposedPersonTypeRule"
PoliticallyExposedPerson <PltclyXpsdPrsn> contains the following PoliticallyExposedPerson1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PoliticallyExposedPersonType <PltclyXpsdPrsnTp> [1..1]  5089
{Or     Code <Cd> [1..1] CodeSet 5090
Or}     Proprietary <Prtry> [1..1] ± 5090
   PoliticallyExposedPersonStatus <PltclyXpsdPrsnSts> [0..1]  5090
{Or     Code <Cd> [1..1] CodeSet 5090
Or}     Proprietary <Prtry> [1..1] ± 5091
Constraints
• PoliticallyExposedPersonTypeRule
If PoliticallyExposedPersonType/Code is 'NoPoliticalExposure' (NPEX) then
PoliticallyExposedPersonStatus is not allowed.
On Condition
    /PoliticallyExposedPersonType/Code is equal to value 'NoPoliticalExposure'
Following Must be True
    /PoliticallyExposedPersonStatus Must be absent
66.1.32.7.16.1  PoliticallyExposedPersonType <PltclyXpsdPrsnTp>
Presence: [1..1]
Definition: Specifies if due diligence checks on the political exposure of the investor have been carried
out. (A politically exposed person is someone who has been entrusted with a prominent public function,
or an individual who is closely related to such a person.)
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5089 May 2026
```

