---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["39 reda.019.001.01 SecuritiesAccountQueryV01", "39.4 Message Building Blocks", "39.4.2 SearchCriteria <SchCrit>", "39.4.2.1 AccountIdentification <AcctId>"]
file_pages: [2110]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.019.001.01"]
---

# 39.4.2.1 AccountIdentification <AcctId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2110 to 2110.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2110

```text
SearchCriteria <SchCrit> contains the following SecuritiesAccountSearchCriteria2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [0..1] Text 2110
   AccountServicer <AcctSvcr> [0..1] ± 2110
   AccountOwner <AcctOwnr> [0..1] ± 2111
   PartyType <PtyTp> [0..1]  2111
{Or     Code <Cd> [1..1] CodeSet 2111
Or}     Proprietary <Prtry> [1..1] Text 2111
   OpeningDate <OpngDt> [0..1]  2111
{Or     FromDate <FrDt> [1..1] Date 2112
Or     ToDate <ToDt> [1..1] Date 2112
Or     FromToDate <FrToDt> [1..1] ± 2112
Or     EqualDate <EQDt> [1..1] Date 2112
Or}     NotEqualDate <NEQDt> [1..1] Date 2112
   ClosingDate <ClsgDt> [0..1]  2112
{Or     FromDate <FrDt> [1..1] Date 2113
Or     ToDate <ToDt> [1..1] Date 2113
Or     FromToDate <FrToDt> [1..1] ± 2113
Or     EqualDate <EQDt> [1..1] Date 2113
Or}     NotEqualDate <NEQDt> [1..1] Date 2113
   AccountType <AcctTp> [0..1]  2114
{Or     Code <Cd> [1..1] CodeSet 2114
Or}     Proprietary <Prtry> [1..1] ± 2114
   EndInvestorFlag <EndInvstrFlg> [0..1] Text 2115
   PricingScheme <PricgSchme> [0..1] Text 2115
39.4.2.1  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 3328
39.4.2.2  AccountServicer <AcctSvcr>
Presence: [0..1]
Definition: Party that services the account.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.019.001.01 SecuritiesAccountQueryV01
Target2-Securities 2110 August 2026
```

