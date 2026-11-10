---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["3 reda.019.001.01 SecuritiesAccountQueryV01", "3.4 Message Building Blocks", "3.4.2 SearchCriteria <SchCrit>", "3.4.2.8 EndInvestorFlag <EndInvstrFlg>"]
file_pages: [23]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.019.001.01"]
---

# 3.4.2.8 EndInvestorFlag <EndInvstrFlg>

Source: [src-000372](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 23 to 23.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 23

```text
3.4.2.8  EndInvestorFlag <EndInvstrFlg>
Presence: [0..1]
Definition: Specifies information to identify securities accounts where allocation instructions are posted.
Datatype: "Exact4AlphaNumericText" on page 99
3.4.2.9  PricingScheme <PricgSchme>
Presence: [0..1]
Definition: Defines how the price is applied to the securities account.
Datatype: "Exact4AlphaNumericText" on page 99
3.4.3 ReturnCriteria <RtrCrit>
Presence: [0..1]
Definition: Defines the expected securities account reference data to be returned.
ReturnCriteria <RtrCrit> contains the following SecuritiesAccountReturnCriteria1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [0..1] Indicator 23
   PartyIdentification <PtyId> [0..1] Indicator 23
   PartyType <PtyTp> [0..1] Indicator 24
   AccountServicer <AcctSvcr> [0..1] Indicator 24
   AccountType <AcctTp> [0..1] Indicator 24
   OpeningDate <OpngDt> [0..1] Indicator 24
   ClosingDate <ClsgDt> [0..1] Indicator 24
   EndInvestorFlag <EndInvstrFlg> [0..1] Indicator 25
   PricingScheme <PricgSchme> [0..1] Indicator 25
3.4.3.1  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Indicates whether the identification of the account is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 98):
• Meaning When True: Requested
• Meaning When False: Not Requested
3.4.3.2  PartyIdentification <PtyId>
Presence: [0..1]
Definition: Indicates whether the identification of the party owning the account is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 98):
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.019.001.01 SecuritiesAccountQueryV01
Target2-Securities - Securities Account Reference Data 23 December 2019
```

