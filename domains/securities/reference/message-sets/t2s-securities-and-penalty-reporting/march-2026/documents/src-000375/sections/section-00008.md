---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["2 semt.025.001.01 SecuritiesAccountPositionQueryV01", "2.4 Message Building Blocks", "2.4.2 SearchCriteria <SchCrit>", "2.4.2.4 FinancialInstrument <FinInstrm>"]
file_pages: [9]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.025.001.01"]
---

# 2.4.2.4 FinancialInstrument <FinInstrm>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 9 to 9.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 9

```text
Definition: Account to or from which a securities entry is made.
SafekeepingAccount <SfkpgAcct> contains one of the following elements (see
"SecuritiesAccount2Choice" on page 248 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Range <Rg> [1..1]  248
     From <Fr> [1..1] ± 249
     To <To> [1..1] ± 249
Or}   Account <Acct> [1..*] ± 249
2.4.2.4  FinancialInstrument <FinInstrm>
Presence: [0..1]
Definition: Financial instrument representing a sum of rights of the investor vis-à-vis the issuer.
Impacted by: C4 "DescriptionPresenceRule", C5 "DescriptionUsageRule", C7 "ISINGuideline", C8
"ISINPresenceRule", C9 "OtherIdentificationPresenceRule"
FinancialInstrument <FinInstrm> contains the following elements (see "SecurityIdentification19" on
page 339 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 340
   OtherIdentification <OthrId> [0..*]  340
     Identification <Id> [1..1] Text 340
     Suffix <Sfx> [0..1] Text 340
     Type <Tp> [1..1] ± 341
   Description <Desc> [0..1] Text 341
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
Approved by the Securities SEG 19 February 2026. semt.025.001.01
SecuritiesAccountPositionQueryV01
Target2-Securities - Securities and Penalty Reporting 9 March 2026
```

