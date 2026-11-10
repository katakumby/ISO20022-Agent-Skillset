---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["70 semt.025.001.01 SecuritiesAccountPositionQueryV01", "70.4 Message Building Blocks", "70.4.2 SearchCriteria <SchCrit>", "70.4.2.4 FinancialInstrument <FinInstrm>"]
file_pages: [2405]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.025.001.01"]
---

# 70.4.2.4 FinancialInstrument <FinInstrm>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2405 to 2405.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2405

```text
Definition: Account to or from which a securities entry is made.
SafekeepingAccount <SfkpgAcct> contains one of the following elements (see
"SecuritiesAccount2Choice" on page 2835 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Range <Rg> [1..1]  2835
     From <Fr> [1..1] ± 2836
     To <To> [1..1] ± 2836
Or}   Account <Acct> [1..*] ± 2836
70.4.2.4  FinancialInstrument <FinInstrm>
Presence: [0..1]
Definition: Financial instrument representing a sum of rights of the investor vis-à-vis the issuer.
Impacted by: C4 "DescriptionPresenceRule", C5 "DescriptionUsageRule", C7 "ISINGuideline", C8
"ISINPresenceRule", C9 "OtherIdentificationPresenceRule"
FinancialInstrument <FinInstrm> contains the following elements (see "SecurityIdentification19" on
page 2951 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 2952
   OtherIdentification <OthrId> [0..*]  2952
     Identification <Id> [1..1] Text 2952
     Suffix <Sfx> [0..1] Text 2952
     Type <Tp> [1..1] ± 2952
   Description <Desc> [0..1] Text 2953
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
• DescriptionUsageRule
Description must be used alone as the last resort.
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.025.001.01
SecuritiesAccountPositionQueryV01
Target2-Securities 2405 August 2026
```

