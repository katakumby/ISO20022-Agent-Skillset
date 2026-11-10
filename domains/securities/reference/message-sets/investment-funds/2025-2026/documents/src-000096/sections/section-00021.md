---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["3 acmt.002.001.08 AccountDetailsConfirmationV08", "3.4 Message Building Blocks", "3.4.3 RelatedReference <RltdRef>"]
file_pages: [44]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.002.001.08"]
---

# 3.4.3 RelatedReference <RltdRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 44 to 44.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 44

```text
OrderReference <OrdrRef> contains the following elements (see "InvestmentFundOrder4" on
page 4754 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OrderReference <OrdrRef> [0..1] Text 4754
   MasterReference <MstrRef> [0..1] Text 4754
3.4.3 RelatedReference <RltdRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously received.
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference13" on
page 4546 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4546
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4547
3.4.4 ConfirmationDetails <ConfDtls>
Presence: [1..1]
Definition: Information about the request or instruction which triggered this confirmation.
ConfirmationDetails <ConfDtls> contains the following AccountManagementConfirmation5
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ConfirmationType <ConfTp> [1..1] ± 44
   AccountApplicationIdentification <AcctApplId> [0..1] Text 45
   ClientReference <ClntRef> [0..1] Text 45
   CounterpartyReference <CtrPtyRef> [0..1] ± 45
   ExistingAccountIdentification <ExstgAcctId> [0..*] ± 45
3.4.4.1  ConfirmationType <ConfTp>
Presence: [1..1]
Definition: Specifies the confirmation type.
Approved by the Securities SEG on 27 January 2026 acmt.002.001.08 AccountDetailsConfirmationV08
Investment Funds - Maintenance 2025 - 2026 44 May 2026
```

