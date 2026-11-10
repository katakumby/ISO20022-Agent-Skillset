---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["39 reda.019.001.01 SecuritiesAccountQueryV01", "39.4 Message Building Blocks", "39.4.2 SearchCriteria <SchCrit>", "39.4.2.8 EndInvestorFlag <EndInvstrFlg>"]
file_pages: [2115]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.019.001.01"]
---

# 39.4.2.8 EndInvestorFlag <EndInvstrFlg>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2115 to 2115.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2115

```text
39.4.2.8  EndInvestorFlag <EndInvstrFlg>
Presence: [0..1]
Definition: Specifies information to identify securities accounts where allocation instructions are posted.
Datatype: "Exact4AlphaNumericText" on page 3325
39.4.2.9  PricingScheme <PricgSchme>
Presence: [0..1]
Definition: Defines how the price is applied to the securities account.
Datatype: "Exact4AlphaNumericText" on page 3325
39.4.3 ReturnCriteria <RtrCrit>
Presence: [0..1]
Definition: Defines the expected securities account reference data to be returned.
ReturnCriteria <RtrCrit> contains the following SecuritiesAccountReturnCriteria1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [0..1] Indicator 2115
   PartyIdentification <PtyId> [0..1] Indicator 2115
   PartyType <PtyTp> [0..1] Indicator 2116
   AccountServicer <AcctSvcr> [0..1] Indicator 2116
   AccountType <AcctTp> [0..1] Indicator 2116
   OpeningDate <OpngDt> [0..1] Indicator 2116
   ClosingDate <ClsgDt> [0..1] Indicator 2116
   EndInvestorFlag <EndInvstrFlg> [0..1] Indicator 2117
   PricingScheme <PricgSchme> [0..1] Indicator 2117
39.4.3.1  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Indicates whether the identification of the account is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 3323):
• Meaning When True: Requested
• Meaning When False: Not Requested
39.4.3.2  PartyIdentification <PtyId>
Presence: [0..1]
Definition: Indicates whether the identification of the party owning the account is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 3323):
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.019.001.01 SecuritiesAccountQueryV01
Target2-Securities 2115 August 2026
```

