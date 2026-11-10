---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["4 acmt.003.001.08 AccountModificationInstructionV08", "4.4 Message Building Blocks", "4.4.3 InstructionDetails <InstrDtls>", "4.4.3.5 ExistingAccountIdentification <ExstgAcctId>"]
file_pages: [65]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.003.001.08"]
---

# 4.4.3.5 ExistingAccountIdentification <ExstgAcctId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 65 to 65.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 65

```text
CounterpartyReference <CtrPtyRef> contains the following elements (see "AdditionalReference13"
on page 4546 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4546
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4547
4.4.3.5  ExistingAccountIdentification <ExstgAcctId>
Presence: [0..*]
Definition: Account to which the account opening is related.
ExistingAccountIdentification <ExstgAcctId> contains the following elements (see "Account23" on
page 4325 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1] Text 4325
   RelatedAccountDetails <RltdAcctDtls> [0..1] ± 4325
4.4.4 InvestmentAccountSelection <InvstmtAcctSelctn>
Presence: [1..1]
Definition: Identifies the account for which the information is modified.
InvestmentAccountSelection <InvstmtAcctSelctn> contains one of the following
AccountSelection3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AccountIdentification <AcctId> [1..1] Text 65
Or}   OtherAccountSelectionData <OthrAcctSelctnData> [1..1] ± C1 65
4.4.4.1  AccountIdentification <AcctId>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
4.4.4.2  OtherAccountSelectionData <OthrAcctSelctnData>
Presence: [1..1]
Definition: Various investment account information used to select a specific account.
Impacted by: C1 "AccountDataElementRule"
Approved by the Securities SEG on 27 January 2026 acmt.003.001.08 AccountModificationInstructionV08
Investment Funds - Maintenance 2025 - 2026 65 May 2026
```

